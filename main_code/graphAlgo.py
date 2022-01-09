import json
import random

import math
import sys
from math import sqrt

from classes.agent import Agent
from classes.edge import Edge
from classes.node import Node
from classes.pokemon import Pokemons
from classes.position import Position


class GraphAlgo:
    Nodes = {}
    Edges = []
    distances = {}
    pokemons = []
    agents = []

    def __init__(self):
        self.Nodes = {}
        self.Edges = []
        self.distances = {}
        self.center = None
        self.up = []  # (src= 10 , dest= 0 , w= 1.1761238717867548)
        self.down = []
        self.pokemons = []
        self.agents = []

    def load_json(self, file_name: str) -> bool:
        """
        Loads a graph from a json file.
        :param file_name: the json file
        :return True if the loading was successful, False o.w.
        """
        flag = True
        try:
            my_dict = json.loads(file_name)
            list_Nodes = my_dict["Nodes"]
            list_Edges = my_dict["Edges"]

            for v in list_Nodes:
                if len(v) == 1:
                    jpos = None
                else:
                    jpos = tuple(map(float, str(v["pos"]).split(",")))
                    id_num = v["id"]
                    nd = Node(id_num, jpos)
                    self.Nodes[id_num] = nd

            for i in list_Edges:
                ed = Edge(src=i["src"], dest=i["dest"], weight=i["w"])
                src = ed.src
                dest = ed.dest
                self.Edges.append(ed)

                src_pos = self.Nodes[src].pos
                dest_pos = self.Nodes[dest].pos

                if src_pos.y < dest_pos.y:
                    ed.set_tag(1)
                    self.up.insert(0, ed)
                elif src_pos.y > dest_pos.y:
                    ed.set_tag(-1)
                    self.down.insert(0, ed)  # down -

                self.Nodes[src].add_out_edge(ed)
                self.Nodes[dest].add_in_edge(ed)
            self.distances_nodes()
            self.center_point()
        except FileNotFoundError:
            flag = False
            raise FileNotFoundError
        finally:
            return flag

    def load_agents(self, data: str, agentNum: int) -> bool:
        """
        :param data: str of all the agents in the game, the aim is to generate an object from them
        :return: update list of agents
        """
        flag = True
        self.agents.clear()
        try:
            my_dict = json.loads(data)
            for a in my_dict["Agents"]:
                id = a["Agent"]["id"]
                value = a["Agent"]["value"]
                src = a["Agent"]["src"]
                dest = a["Agent"]["dest"]
                speed = a["Agent"]["speed"]
                jpos = tuple(map(float, str(a["Agent"]["pos"]).split(",")))
                jpos = Position(jpos)
                if agentNum == 2:
                    if id == 2:
                        jpos = self.Nodes[self.center].pos

                elif agentNum == 3:
                    if id == 2:
                        jpos = self.Nodes[self.center].pos
                    elif id == 3:
                        jpos = self.Nodes[(int)(random.uniform(1, len(self.Nodes)))].pos
                agent = Agent(id, value, src, dest, speed, jpos)
                self.agents.append(agent)
        except FileNotFoundError:
            flag = False
            raise FileNotFoundError
        finally:
            return flag

    def load_Pokemon(self, data: str) -> bool:
        """
        '{"Pokemons":[{"Pokemon":{"value":5.0,"type":-1,"pos":"35.197656770719604,32.10191878639921,0.0"} },...]}'
        :param data: str
        :return: update the list that we init
        """
        flag = True
        self.pokemons.clear()
        try:
            my_dict = json.loads(data)
            for p in my_dict["Pokemons"]:
                value = p["Pokemon"]['value']
                type = p["Pokemon"]['type']
                jpos = tuple(map(float, str(p["Pokemon"]['pos']).split(",")))
                edge = self.find_edge(jpos, type)
                poc = Pokemons(value, type, jpos)
                poc.edge = edge
                self.pokemons.append(poc)

        except FileNotFoundError:
            flag = False
            raise FileNotFoundError
        finally:
            return flag

    def is_between(self, a, c, b) -> bool:
        """
        check if the point (c) is between a --> b
        :param a: src
        :param c: check point
        :param b: dest
        :return: true / false <bound method GraphAlgo.dist of <graphAlgo.GraphAlgo object at 0x0000023904020BB0>>
        """
        return math.isclose(self.dist(a, c) + self.dist(c, b), self.dist(a, b), abs_tol=0.00000000000001)

    def dist(self, a, b) -> float:
        """
        calculate the dist between them (a & b)
        """
        return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

    def find_edge(self, pocPos: tuple, type: int):
        """
        this function find the edge (sec + dest) that the Pokemon is on
        :param pocPos: position of the Pokemon
        :param type: up / down
        :return: the edge that the Pokemon is on
        """
        if type == -1:
            for i in self.down:
                src = i.src
                dest = i.dest
                pSrc = self.Nodes.get(src).pos
                pDest = self.Nodes.get(dest).pos
                ans = self.is_between(pSrc, pocPos, pDest)
                if ans:
                    return i
                else:
                    continue
        else:
            for i in self.up:
                src = i.src
                dest = i.dest
                pSrc = self.Nodes.get(src).pos
                pDest = self.Nodes.get(dest).pos
                ans = self.is_between(pSrc, pocPos, pDest)
                if ans:
                    return i
                else:
                    continue
        return None

    def shortest_path(self, id1: int, id2: int):

        """
        :param id1: src node
        :param id2: dest node
        :return: The distance of the path, a list of the nodes ids that the path goes through
        """
        if id1 == id2:
            return float('inf'), []

        # src_distances a dict of id1 distances and path to the graph's nodes
        src_distances = {}
        src_distances[id1] = [0, None]
        nodes = self.Nodes
        for current_key in nodes:
            nodes.get(current_key).set_tag(0)

            # id1 is already define in src_distances (line 116)
            if current_key != id1:
                if self.distances is not None \
                        and self.distances.get(id1) is not None \
                        and self.distances.get(id1).get(current_key) is not None:
                    src_distances[current_key] = self.distances.get(id1).get(current_key)

                # if there's an edge between src and dest then put the weight of the edge
                elif nodes.get(id1).get_edge(current_key) is not None:
                    temp_path = [id1, current_key]
                    src_distances[current_key] = [nodes.get(id1).get_edge(current_key).weight, temp_path]
                else:
                    src_distances[current_key] = [sys.float_info.max, None]

        while nodes.get(id2).tag != 1:
            # getting the node with the lowest distance from id1
            index = self.lowest_dist(src_distances, nodes)
            if index == -1:
                return float('inf'), []
            else:
                self.dijkstra_algorithm(index, src_distances)
                nodes.get(index).set_tag(1)

        self.distances[id1] = src_distances

    def lowest_dist(self, src_distances: dict, nodes: dict) -> int:
        """
        :param nodes: dictionary of the graph's nodes
        :param src_distances: dictionary with the src distances to the other nodes in the graph
        :return: The index of the node with the lowest distance from src node
        """
        temp_dist = sys.float_info.max
        ans = -1

        for i in src_distances:
            key = i
            value = src_distances[key][0]

            current_node = nodes.get(key)
            if current_node.tag == 0:
                if value < temp_dist:
                    temp_dist = value
                    ans = key
        return ans

    def dijkstra_algorithm(self, index: int, src_distances: dict) -> None:
        """
        :param index: current node to check
        :param src_distances: src_distances: dictionary with the src distances to the other nodes in the graph
        :return: void, updating src_distances if theres a new lower distance
        """
        dist = src_distances[index][0]
        edges = self.Nodes[index].outEdges

        for e in edges:
            dest_node = edges[e].dest
            new_dist = dist + edges[e].weight

            if new_dist < src_distances[dest_node][0]:
                temp_list = src_distances[index][1]
                src_distances[dest_node] = [new_dist, [x for x in temp_list]]
                src_distances[dest_node][1].append(dest_node)

    def distances_nodes(self):
        for current_key in self.Nodes:
            for next_node in self.Nodes:
                if current_key != next_node:
                    if self.distances is not None \
                            and self.distances.get(current_key) is not None \
                            and self.distances.get(current_key).get(next_node) is not None \
                            and self.distances.get(current_key).get(next_node)[0] is not None \
                            and self.distances.get(current_key).get(next_node)[0] != sys.float_info.max:
                        continue
                    else:
                        self.shortest_path(current_key, next_node)

    def center_point(self) -> (int, float):
        """
            Finds the node that has the shortest distance to it's farthest node.
            :return: The nodes id, min-maximum distance
            """

        min_value = sys.float_info.max
        answer = 0

        for current_key in self.Nodes:
            temp_max = 0
            max_value = sys.float_info.min

            for next_node in self.Nodes:
                if current_key != next_node:
                    temp_max = self.distances.get(current_key).get(next_node)[0]

                    # getting the max value of the current node distances
                    if temp_max > max_value:
                        max_value = temp_max

            if max_value < min_value:
                min_value = max_value
                answer = current_key

        self.center = answer
        return answer

    def allocateAgent(self, agent: Agent):
        """
        this method allocate agent to specific pokemon
        :param agent: the agent that we want to work on
        :return:
        """
        speed = agent.speed
        minDist = float('inf')
        minPath = []
        dist = -1
        pos = -1
        pokemon = None
        for pok in self.pokemons:
            if pok.myAgent != agent.id:
                if pok.myAgent != -1:
                    continue
            dest = pok.edge.dest
            dist, path = self.distances[agent.src][dest]
            if not path:
                dist = 0.0
            else:
                dist = float(dist) / speed
            if float(dist) < minDist:
                minDist = dist
                minPath = path
                pos = pok.pos
        if dist == -1:
            return dist, None, None
        for p in self.pokemons:
            if pos == p.pos:
                p.set_agent(agent.id)
                pokemon = p
        return minDist, minPath, pokemon

    def getMin(self):
        maxX = float('-inf')
        minX = float('inf')
        maxY = float('-inf')
        minY = float('inf')
        for n in self.Nodes.values():
            if float(n.pos[0]) > maxX:
                maxX = float(n.pos[0])
            if float(n.pos[0]) < minX:
                minX = float(n.pos[0])
            if float(n.pos[1]) > maxY:
                maxY = float(n.pos[1])
            if float(n.pos[1]) < minY:
                minY = float(n.pos[1])
        return maxX, minX, maxY, minY
