from numpy import random

from Edge import Edge
from position import Position


class Node:

    def __init__(self, id_num: int, position: tuple):
        """
        :param id_num: uniq key of the node
        :param position: geo position
        """
        self.key = id_num
        if position is not None:
            self.pos = Position(position)
        else:
            x = random.uniform(0.0, 100)
            y = random.uniform(0.0, 100)
            p = Position((x, y, 0))
            self.pos = p

    def get_key(self) -> int:
        return self.key

    def __str__(self) -> str:
        return f"{self.key}: |edge_out| {len(self.outEdges)} |edge_in| {len(self.inEdges.keys())}"

    def __repr__(self) -> str:
        return f"{self.key}: |edge_out| {len(self.outEdges)} |edge_in| {len(self.inEdges.keys())}"