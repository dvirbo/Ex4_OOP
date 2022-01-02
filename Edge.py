class edge:

    def __init__(self, src: int, dest: int, weight: float):
        self.src = src
        self.dest = dest
        self.weight = weight
        self.tag = 0

    def set_tag(self, t: int):
        self.tag = t
