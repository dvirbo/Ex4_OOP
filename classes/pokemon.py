class Pokemons:
    def __init__(self, value: float = None, type: int = None, pos: tuple = None) -> None:
        """
        the class get  the current pokemons state as json str.
        for pokemon lying on edge (src,dest), then:
        src < dest => type > 0
        dest < src => type < 0
        example:
        {
            "Pokemons":[
                {
                    "Pokemon":{
                        "value":5.0,
                        "type":-1,
                        "pos":"35.197656770719604,32.10191878639921,0.0"
                    }
                }
            ]
        }

        """
        self.value = value
        self.type = type
        self.pos = pos
        self.edge = None
        self.src = None
        self.dest = None

    def __str__(self) -> str:
        return f""" pokemon: value= {self.value} , type= {self.type} , pos= {self.pos}"""

    def __repr__(self) -> str:
        return f""" pokemon: value= {self.value} , type= {self.type} , pos= {self.pos}"""
