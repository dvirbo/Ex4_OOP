import json
import sys

from classes.edge import Edge
from classes.node import Node
from queue import PriorityQueue

from classes.pokemon import Pokemons


class GraphAlgo:
    Nodes = {}
    distances = {}
    pokemons = []

    def __init__(self):
        self.Nodes = {}
        self.distances = {}
        self.up_down = {}

    def load_json(self, file_name: str):
        """
        Loads a graph from a json file.
        :param file_name: The path to the json file
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

                src_pos = self.Nodes[src].pos
                dest_pos = self.Nodes[dest].pos

                if src_pos.y < dest_pos.y:
                    ed.set_tag(1)
                    self.up_down[1].apeand(ed)
                elif src_pos.y > dest_pos.y:
                    ed.set_tag(-1)
                    self.up_down[-1].apeand(ed)

                self.Nodes[src].add_out_edge(ed)
                self.Nodes[dest].add_in_edge(ed)

        except FileNotFoundError:
            flag = False
            raise FileNotFoundError
        finally:
            return flag

    def load_Pokemon(self, file_name: str):
        """
        '{"Pokemons":[{"Pokemon":{"value":5.0,"type":-1,"pos":"35.197656770719604,32.10191878639921,0.0"} },  ]}'
         {"Edges":[{"src":0,"w":1.4004465106761335,"dest":1},{"src":0,"w":1.4620268165085584,"dest":10},{"src":1,"w":1.8884659521433524,"dest":0},{"src":1,"w":1.7646903245689283,"dest":2},{"src":2,"w":1.7155926739282625,"dest":1},{"src":2,"w":1.1435447583365383,"dest":3},{"src":3,"w":1.0980094622804095,"dest":2},{"src":3,"w":1.4301580756736283,"dest":4},{"src":4,"w":1.4899867265011255,"dest":3},{"src":4,"w":1.9442789961315767,"dest":5},{"src":5,"w":1.4622464066335845,"dest":4},{"src":5,"w":1.160662656360925,"dest":6},{"src":6,"w":1.6677173820549975,"dest":5},{"src":6,"w":1.3968360163668776,"dest":7},{"src":7,"w":1.0176531013725074,"dest":6},{"src":7,"w":1.354895648936991,"dest":8},{"src":8,"w":1.6449953452844968,"dest":7},{"src":8,"w":1.8526880332753517,"dest":9},{"src":9,"w":1.4575484853801393,"dest":8},{"src":9,"w":1.022651770039933,"dest":10},{"src":10,"w":1.1761238717867548,"dest":0},{"src":10,"w":1.0887225789883779,"dest":9}],
         "Nodes":[{"pos":"35.18753053591606,32.10378225882353,0.0","id":0},{"pos":"35.18958953510896,32.10785303529412,0.0","id":1},{"pos":"35.19341035835351,32.10610841680672,0.0","id":2},{"pos":"35.197528356739305,32.1053088,0.0","id":3},{"pos":"35.2016888087167,32.10601755126051,0.0","id":4},{"pos":"35.20582803389831,32.10625380168067,0.0","id":5},{"pos":"35.20792948668281,32.10470908739496,0.0","id":6},{"pos":"35.20746249717514,32.10254648739496,0.0","id":7},{"pos":"35.20319591121872,32.1031462,0.0","id":8},{"pos":"35.19597880064568,32.10154696638656,0.0","id":9},{"pos":"35.18910131880549,32.103618700840336,0.0","id":10}]}
        :param file_name: str
        :return: update the list that we init

                     {'value': 5.0, 'type': -1, 'pos': '35.197656770719604,32.10191878639921,0.0'}
                     jpos = tuple(map(float, str(v["pos"]).split(",")))
                    id_num = v["id"]
                    nd = Node(id_num, jpos)
                    self.Nodes[id_num] = nd
        """
        flag = True
        try:
            my_dict = json.loads(file_name)
            poc_list = my_dict["Pokemons"]
            for p in poc_list:
                value = poc_list["Pokemon"]['value']
                type = poc_list["Pokemon"]['type']
                jpos = poc_list["Pokemon"]['pos']
                poc = Pokemons(value, type, jpos)
                self.pokemons[p] = poc


        except FileNotFoundError:
            flag = False
            raise FileNotFoundError
        finally:
            return flag

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        :param id1: src node
        :param id2: dest node
        :return: The distance of the path, a list of the nodes ids that the path goes through
        """
        if id1 == id2:
            return float('inf'), []

        # checking if self.distance has the answer
        if self.distances is not None \
                and self.distances.get(id1) is not None \
                and self.distances.get(id1).get(id2) is not None \
                and self.distances.get(id1).get(id2)[0] is not None \
                and self.distances.get(id1).get(id2)[0] != sys.float_info.max \
                and self.distances.get(id1).get(id2)[1] is not None:
            return self.distances.get(id1).get(id2)

        # src_distances a dict of id1 distances and path to the graph's nodes
        src_distances = {}
        src_distances[id1] = [0, None]
        p_queue = PriorityQueue()
        nodes = self.Nodes
        for current_key in nodes:
            nodes.get(current_key).set_tag(0)

            # id1 is already define in src_distances (line 116)
            if current_key != id1:
                if self.distances is not None \
                        and self.distances.get(id1) is not None \
                        and self.distances.get(id1).get(current_key) is not None:
                    temp = self.distances.get(id1).get(current_key)
                    src_distances[current_key] = temp
                    p_queue.put((temp, current_key))

                # if there's an edge between src and dest then put the weight of the edge
                elif nodes.get(id1).get_edge(current_key) is not None:
                    temp_path = [id1, current_key]
                    temp = nodes.get(id1).get_edge(current_key).weight
                    src_distances[current_key] = [temp, temp_path]
                    p_queue.put((temp, current_key))
                else:
                    src_distances[current_key] = [sys.float_info.max, None]
                    p_queue.put((sys.float_info.max, current_key))

        while self.Nodes[id2].tag != 1:
            # getting the node with the lowest distance from id1
            temp = p_queue.get()
            index = temp[1]
            self.dijkstra_algorithm(index, src_distances)
            nodes.get(index).set_tag(1)

        self.distances[id1] = src_distances
        return src_distances[id2]

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


if __name__ == "__main__":
    graph = GraphAlgo()
    graph.load_json("data/A3")
    print(graph.shortest_path(6, 30))
