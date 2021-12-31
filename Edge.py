class Edge:
    src = None
    dest = None
    weight = None

    def __init__(self, src: int, dest: int, weight: float):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __str__(self) -> str:
        return f"{self.weight}"

    def __repr__(self) -> str:
        return f"{self.weight}"