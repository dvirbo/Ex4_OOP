class graphAlgo:

    Nodes = {}
    Edges = {}

    def __init__(self):
        self.Nodes = {}
        self.Edges = {}

    def load_json(self, file_name: str):
        """
                         Loads a graph from a json file.
                        :param file_name: The path to the json file
                        :return True if the loading was successful, False o.w.
                        """
        flag = True
        try:
            with open(file_name, "r") as f:
                my_dict = json.load(f)
                list_Nodes = my_dict["Nodes"]
                list_Edges = my_dict["Edges"]
                for v in list_Nodes:
                    if len(v) == 1:
                        jpos = None
                    else:
                        jpos = tuple(map(float, str(v["pos"]).split(",")))
                    id_num = v["id"]
                    node = Node(id_num, jpos)
                    self.Nodes.apeand(node)

                for i in list_Edges:
                    edge = Edge(src=i["src"], dest=i["dest"], weight=i["w"])
                    self.Edges.apeand(edge)
        except FileNotFoundError:
            flag = False
            raise FileNotFoundError
        finally:
            return flag
