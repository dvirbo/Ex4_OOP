from classes.position import Position


class Agent:
    def __init__(self, id=None, value=None, src=None, dest=None, speed=None, pos=None) -> None:
        self.id = id
        self.value = value
        self.src = src
        self.dest = dest
        self.speed = speed
        self.pos = Position(pos)

    def __str__(self) -> str:
        return f""" Agent(id= {self.id} , value= {self.value} , src= {self.src}, dest= {self.dest},  speed= {self.speed} ,pos = {self.pos}  ) """

    def __repr__(self) -> str:
        return f""" Agent(id= {self.id} , value= {self.value} , src= {self.src}, dest= {self.dest},  speed= {self.speed} ,pos = {self.pos}  )"""


