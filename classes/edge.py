class Edge:

    def __init__(self, src: int, dest: int, weight: float):
        self.src = src
        self.dest = dest
        self.weight = weight
        self.tag = 0

    def set_tag(self, t: int):
        self.tag = t

    def __str__(self) -> str:
        return f"""({self.src} ,{self.dest} ,{self.weight}) """

    def __repr__(self) -> str:
        return f"""({self.src} ,{self.dest} ,{self.weight}) """
