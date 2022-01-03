from numpy import random
from classes.edge import Edge
from classes.position import Position


class Node:

    def __init__(self, id_num: int, pos: tuple):
        """
        :param id_num: uniq key of the node
        :param position: geo position
        """
        self.key = id_num
        self.tag = 0
        self.inEdges = {}
        self.outEdges = {}
        if pos is not None:
            self.pos = Position(pos)
        else:
            x = random.uniform(0.0, 100)
            y = random.uniform(0.0, 100)
            p = Position((x, y, 0))
            self.pos = p

    def set_tag(self, t: int):
        self.tag = t

    def get_key(self) -> int:
        return self.key

    def get_edge(self, id2: int):
        try:
            return self.outEdges[id2]
        except KeyError:
            return None

    def __contains__(self, key):
        """
        this function check if the key part of the dict of the nodes
        :param key: the key of the uniq node
        :return: true of the dictionary of the nodes contain the key
        """
        return key in self.outEdges

    def add_out_edge(self, e: Edge):
        id2 = e.dest
        w = e.weight
        if w >= 0:
            if self.__contains__(id2):  # check if e is in the dict nodes
                if self.get_edge(id2).weight > w:
                    self.outEdges[id2].weight = w
            else:
                self.outEdges[id2] = e

    def add_in_edge(self, e: Edge):
        id1 = e.src
        weight = e.weight
        if weight >= 0:
            if id1 in self.inEdges:  # check if e is in the dict nodes
                if self.inEdges[id1][2] > weight:
                    self.inEdges[id1][2] = weight
            else:
                self.inEdges[id1] = e

