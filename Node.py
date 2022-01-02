from numpy import random

from Edge import edge
from Position import position


class node:

    def __init__(self, id_num: int, pos: tuple):
        """
        :param id_num: uniq key of the node
        :param position: geo position
        """
        self.key = id_num
        self.inEdges = {}
        self.outEdges = {}
        if pos is not None:
            self.pos = position(pos)
        else:
            x = random.uniform(0.0, 100)
            y = random.uniform(0.0, 100)
            p = position((x, y, 0))
            self.pos = p

    def get_key(self) -> int:
        return self.key

    def get_edge(self, id2: int):
        try:
            return self.outEdges[id2]
        except KeyError:
            return None

    def add_out_edge(self, id2: int, weight: float):
        if weight >= 0:
            if self.__contains__(id2):  # check if there in the dict nodes
                if self.get_edge(id2).weight > weight:
                    self.outEdges[id2].weight = weight
            else:
                self.outEdges[id2] = edge(self.key, id2, weight)

    def add_in_edge(self, id1: int, weight: float):
        if weight >= 0:
            if id1 in self.inEdges:  # check if there in the dict nodes
                if self.inEdges[id1][2] > weight:
                    self.inEdges[id1][2] = weight
            else:
                self.inEdges[id1] = edge(id1, self.key, weight)