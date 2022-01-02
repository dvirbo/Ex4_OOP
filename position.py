import math


class Position(tuple):
    """
    this class represent a position point in 3D dimension
    """

    def __init__(self, pos: tuple = None):
        """
        :param pos: constructor that get tuple of 3 parameters: x, y, z
        """
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
