import json
import sys

from classes.edge import Edge
from classes.node import Node
from queue import PriorityQueue


class GraphAlgo:
    Nodes = {}
    distances = {}

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
    graph = graphAlgo()
    graph.load_json("data/A3")
    print(graph.shortest_path(6, 30))
