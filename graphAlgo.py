import json

from Edge import edge
from node import Node


class GraphAlgo:
    Nodes = {}

    def __init__(self):
        self.Nodes = {}

    def load_json(self, file_name: str):
        """
         Loads a graph from a json file.
         :param file_name: The path to the json file
         :return True if the loading was successful, False o.w.
        """
        flag = True
        try:
            data = json.loads(file_name)
            list_Nodes = data["Nodes"]
            list_Edges = data["Edges"]

            for v in list_Nodes:
                if len(v) == 1:
                    jpos = None
                else:
                    jpos = tuple(map(float, str(v["pos"]).split(",")))
                id_num = v["id"]
                nd = Node(id_num, jpos)
                self.Nodes[id_num] = nd

            for i in list_Edges:
                ed = edge(src=i["src"], dest=i["dest"], weight=i["w"])
                self.Nodes[ed.src].add_out_edge(ed.dest, ed.weight)
                self.Nodes[ed.dest].add_in_edge(ed.src, ed.weight)

        except FileNotFoundError:
            flag = False
            raise FileNotFoundError
        finally:
            return flag
