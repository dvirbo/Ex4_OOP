import math


class position(tuple):
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

    def __repr__(self):
        return f"{self.x}, {self.y}, {self.z}"

    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"