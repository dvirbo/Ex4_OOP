import json
import unittest
from unittest import TestCase

from classes.edge import Edge
from classes.node import Node
from main_code.graphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    if __name__ == '__main__':
        unittest.main()


class TestGraphAlgo(TestCase):
    def test_find_edge(self):
        g = GraphAlgo()
        for n in range(11):
            pos = (0, 0, 0)
            g.Nodes[n] = Node(n, pos)

        g.Nodes[0].pos = (35.18753053591606, 32.10378225882353, 0.0)
        g.Nodes[1].pos = (35.18958953510896, 32.10785303529412, 0.0)
        g.Nodes[2].pos = (35.19341035835351,32.10610841680672,0.0)
        g.Nodes[3].pos = (35.197528356739305,32.1053088,0.0)
        g.Nodes[4].pos = (35.2016888087167,32.10601755126051,0.0)
        g.Nodes[5].pos = (35.20582803389831,32.10625380168067,0.0)
        g.Nodes[6].pos = (35.20792948668281,32.10470908739496,0.0)
        g.Nodes[7].pos = (35.20746249717514,32.10254648739496,0.0)
        g.Nodes[8].pos = (35.20319591121872,32.1031462,0.0)
        g.Nodes[9].pos = (35.19597880064568,32.10154696638656,0.0)
        g.Nodes[10].pos = (35.18910131880549,32.103618700840336,0.0)

        e1 = Edge(0, 1, 1.4004465106761335)
        g.Nodes[0].add_out_edge(e1)
        g.Nodes[1].add_in_edge(e1)
        g.Edges.append(e1)

        e2 = Edge(0, 10, 1.4620268165085584)
        g.Nodes[0].add_out_edge(e2)
        g.Nodes[10].add_in_edge(e2)
        g.Edges.append(e2)

        e3 = Edge(1, 0, 1.8884659521433524)
        g.Nodes[1].add_out_edge(e3)
        g.Nodes[0].add_in_edge(e3)
        g.Edges.append(e3)

        e4 = Edge(1, 2, 1.8884659521433524)
        g.Nodes[1].add_out_edge(e4)
        g.Nodes[2].add_in_edge(e4)
        g.Edges.append(e4)

        e5 = Edge(2, 3, 1.7155926739282625)
        g.Nodes[2].add_out_edge(e5)
        g.Nodes[3].add_in_edge(e5)
        g.Edges.append(e5)

        e6 = Edge(3, 2, 1.143544758336538)
        g.Nodes[3].add_out_edge(e6)
        g.Nodes[2].add_in_edge(e6)
        g.Edges.append(e6)

        e7 = Edge(3, 4, 1.4301580756736283)
        g.Nodes[3].add_out_edge(e7)
        g.Nodes[4].add_in_edge(e7)
        g.Edges.append(e7)

        e8 = Edge(4, 3, 1.4899867265011255)
        g.Nodes[4].add_out_edge(e8)
        g.Nodes[3].add_in_edge(e8)
        g.Edges.append(e8)

        e9 = Edge(4, 5, 1.9442789961315767)
        g.Nodes[4].add_out_edge(e9)
        g.Nodes[5].add_in_edge(e9)
        g.Edges.append(e9)

        e10 = Edge(5, 4, 1.4622464066335845)
        g.Nodes[5].add_out_edge(e10)
        g.Nodes[4].add_in_edge(e10)
        g.Edges.append(e10)

        e11 = Edge(5, 6, 1.160662656360925)
        g.Nodes[5].add_out_edge(e11)
        g.Nodes[6].add_in_edge(e11)
        g.Edges.append(e11)

        e12 = Edge(6, 5, 1.6677173820549975)
        g.Nodes[6].add_out_edge(e12)
        g.Nodes[5].add_in_edge(e12)
        g.Edges.append(e12)

        e13 = Edge(7, 6, 1.0176531013725074)
        g.Nodes[7].add_out_edge(e13)
        g.Nodes[6].add_in_edge(e13)
        g.Edges.append(e13)

        e14 = Edge(6, 7, 1.3968360163668776)
        g.Nodes[6].add_out_edge(e14)
        g.Nodes[7].add_in_edge(e14)
        g.Edges.append(e14)

        e15 = Edge(7, 8, 1.354895648936991)
        g.Nodes[7].add_out_edge(e15)
        g.Nodes[8].add_in_edge(e15)
        g.Edges.append(e15)

        e16 = Edge(8, 7, 1.6449953452844968)
        g.Nodes[8].add_out_edge(e16)
        g.Nodes[7].add_in_edge(e16)
        g.Edges.append(e16)

        e17 = Edge(8, 9, 1.8526880332753517)
        g.Nodes[8].add_out_edge(e17)
        g.Nodes[9].add_in_edge(e17)
        g.Edges.append(e17)

        e18 = Edge(9, 8, 1.4575484853801393)
        g.Nodes[9].add_out_edge(e18)
        g.Nodes[8].add_in_edge(e18)
        g.Edges.append(e18)

        e19 = Edge(9, 10, 1.022651770039933)
        g.Nodes[9].add_out_edge(e19)
        g.Nodes[10].add_in_edge(e19)
        g.Edges.append(e19)

        e20 = Edge(10, 0, 1.1761238717867548)
        g.Nodes[10].add_out_edge(e20)
        g.Nodes[0].add_in_edge(e20)
        g.Edges.append(e20)

        e21 = Edge(10, 9, 1.0887225789883779)
        g.Nodes[10].add_out_edge(e21)
        g.Nodes[9].add_in_edge(e21)
        g.Edges.append(e21)

        self.assertEqual(g.find_edge((35.18856003551251, 32.105817647058825, 0.0), 1), 7)

    def test_shortest_path(self):
        g = GraphAlgo()
        for n in range(11):
            pos = (0, 0, 0)
            g.Nodes[n] = Node(n, pos)

        e1 = Edge(0, 1, 1.4004465106761335)
        g.Nodes[0].add_out_edge(e1)
        g.Nodes[1].add_in_edge(e1)
        g.Edges.append(e1)

        e2 = Edge(0, 10, 1.4620268165085584)
        g.Nodes[0].add_out_edge(e2)
        g.Nodes[10].add_in_edge(e2)
        g.Edges.append(e2)

        e3 = Edge(1, 0, 1.8884659521433524)
        g.Nodes[1].add_out_edge(e3)
        g.Nodes[0].add_in_edge(e3)
        g.Edges.append(e3)

        e4 = Edge(1, 2, 1.8884659521433524)
        g.Nodes[1].add_out_edge(e4)
        g.Nodes[2].add_in_edge(e4)
        g.Edges.append(e4)

        e5 = Edge(2, 3, 1.7155926739282625)
        g.Nodes[2].add_out_edge(e5)
        g.Nodes[3].add_in_edge(e5)
        g.Edges.append(e5)

        e6 = Edge(3, 2, 1.143544758336538)
        g.Nodes[3].add_out_edge(e6)
        g.Nodes[2].add_in_edge(e6)
        g.Edges.append(e6)

        e7 = Edge(3, 4, 1.4301580756736283)
        g.Nodes[3].add_out_edge(e7)
        g.Nodes[4].add_in_edge(e7)
        g.Edges.append(e7)

        e8 = Edge(4, 3, 1.4899867265011255)
        g.Nodes[4].add_out_edge(e8)
        g.Nodes[3].add_in_edge(e8)
        g.Edges.append(e8)

        e9 = Edge(4, 5, 1.9442789961315767)
        g.Nodes[4].add_out_edge(e9)
        g.Nodes[5].add_in_edge(e9)
        g.Edges.append(e9)

        e10 = Edge(5, 4, 1.4622464066335845)
        g.Nodes[5].add_out_edge(e10)
        g.Nodes[4].add_in_edge(e10)
        g.Edges.append(e10)

        e11 = Edge(5, 6, 1.160662656360925)
        g.Nodes[5].add_out_edge(e11)
        g.Nodes[6].add_in_edge(e11)
        g.Edges.append(e11)

        e12 = Edge(6, 5, 1.6677173820549975)
        g.Nodes[6].add_out_edge(e12)
        g.Nodes[5].add_in_edge(e12)
        g.Edges.append(e12)

        e13 = Edge(7, 6, 1.0176531013725074)
        g.Nodes[7].add_out_edge(e13)
        g.Nodes[6].add_in_edge(e13)
        g.Edges.append(e13)

        e14 = Edge(6, 7, 1.3968360163668776)
        g.Nodes[6].add_out_edge(e14)
        g.Nodes[7].add_in_edge(e14)
        g.Edges.append(e14)

        e15 = Edge(7, 8, 1.354895648936991)
        g.Nodes[7].add_out_edge(e15)
        g.Nodes[8].add_in_edge(e15)
        g.Edges.append(e15)

        e16 = Edge(8, 7, 1.6449953452844968)
        g.Nodes[8].add_out_edge(e16)
        g.Nodes[7].add_in_edge(e16)
        g.Edges.append(e16)

        e17 = Edge(8, 9, 1.8526880332753517)
        g.Nodes[8].add_out_edge(e17)
        g.Nodes[9].add_in_edge(e17)
        g.Edges.append(e17)

        e18 = Edge(9, 8, 1.4575484853801393)
        g.Nodes[9].add_out_edge(e18)
        g.Nodes[8].add_in_edge(e18)
        g.Edges.append(e18)

        e19 = Edge(9, 10, 1.022651770039933)
        g.Nodes[9].add_out_edge(e19)
        g.Nodes[10].add_in_edge(e19)
        g.Edges.append(e19)

        e20 = Edge(10, 0, 1.1761238717867548)
        g.Nodes[10].add_out_edge(e20)
        g.Nodes[0].add_in_edge(e20)
        g.Edges.append(e20)

        e21 = Edge(10, 9, 1.0887225789883779)
        g.Nodes[10].add_out_edge(e21)
        g.Nodes[9].add_in_edge(e21)
        g.Edges.append(e21)

        g.distances_nodes()
        self.assertEqual(g.distances[0][1], [1.4004465106761335, [0, 1]])
        self.assertEqual(g.distances[6][1], [8.203641851082041, [6, 7, 8, 9, 10, 0, 1]])

    def test_center_point(self):
        g = GraphAlgo()
        for n in range(11):
            pos = (0, 0, 0)
            g.Nodes[n] = Node(n, pos)

        e1 = Edge(0, 1, 1.4004465106761335)
        g.Nodes[0].add_out_edge(e1)
        g.Nodes[1].add_in_edge(e1)
        g.Edges.append(e1)

        e2 = Edge(0, 10, 1.4620268165085584)
        g.Nodes[0].add_out_edge(e2)
        g.Nodes[10].add_in_edge(e2)
        g.Edges.append(e2)

        e3 = Edge(1, 0, 1.8884659521433524)
        g.Nodes[1].add_out_edge(e3)
        g.Nodes[0].add_in_edge(e3)
        g.Edges.append(e3)

        e4 = Edge(1, 2, 1.8884659521433524)
        g.Nodes[1].add_out_edge(e4)
        g.Nodes[2].add_in_edge(e4)
        g.Edges.append(e4)

        e5 = Edge(2, 3, 1.7155926739282625)
        g.Nodes[2].add_out_edge(e5)
        g.Nodes[3].add_in_edge(e5)
        g.Edges.append(e5)

        e6 = Edge(3, 2, 1.143544758336538)
        g.Nodes[3].add_out_edge(e6)
        g.Nodes[2].add_in_edge(e6)
        g.Edges.append(e6)

        e7 = Edge(3, 4, 1.4301580756736283)
        g.Nodes[3].add_out_edge(e7)
        g.Nodes[4].add_in_edge(e7)
        g.Edges.append(e7)

        e8 = Edge(4, 3, 1.4899867265011255)
        g.Nodes[4].add_out_edge(e8)
        g.Nodes[3].add_in_edge(e8)
        g.Edges.append(e8)

        e9 = Edge(4, 5, 1.9442789961315767)
        g.Nodes[4].add_out_edge(e9)
        g.Nodes[5].add_in_edge(e9)
        g.Edges.append(e9)

        e10 = Edge(5, 4, 1.4622464066335845)
        g.Nodes[5].add_out_edge(e10)
        g.Nodes[4].add_in_edge(e10)
        g.Edges.append(e10)

        e11 = Edge(5, 6, 1.160662656360925)
        g.Nodes[5].add_out_edge(e11)
        g.Nodes[6].add_in_edge(e11)
        g.Edges.append(e11)

        e12 = Edge(6, 5, 1.6677173820549975)
        g.Nodes[6].add_out_edge(e12)
        g.Nodes[5].add_in_edge(e12)
        g.Edges.append(e12)

        e13 = Edge(7, 6, 1.0176531013725074)
        g.Nodes[7].add_out_edge(e13)
        g.Nodes[6].add_in_edge(e13)
        g.Edges.append(e13)

        e14 = Edge(6, 7, 1.3968360163668776)
        g.Nodes[6].add_out_edge(e14)
        g.Nodes[7].add_in_edge(e14)
        g.Edges.append(e14)

        e15 = Edge(7, 8, 1.354895648936991)
        g.Nodes[7].add_out_edge(e15)
        g.Nodes[8].add_in_edge(e15)
        g.Edges.append(e15)

        e16 = Edge(8, 7, 1.6449953452844968)
        g.Nodes[8].add_out_edge(e16)
        g.Nodes[7].add_in_edge(e16)
        g.Edges.append(e16)

        e17 = Edge(8, 9, 1.8526880332753517)
        g.Nodes[8].add_out_edge(e17)
        g.Nodes[9].add_in_edge(e17)
        g.Edges.append(e17)

        e18 = Edge(9, 8, 1.4575484853801393)
        g.Nodes[9].add_out_edge(e18)
        g.Nodes[8].add_in_edge(e18)
        g.Edges.append(e18)

        e19 = Edge(9, 10, 1.022651770039933)
        g.Nodes[9].add_out_edge(e19)
        g.Nodes[10].add_in_edge(e19)
        g.Edges.append(e19)

        e20 = Edge(10, 0, 1.1761238717867548)
        g.Nodes[10].add_out_edge(e20)
        g.Nodes[0].add_in_edge(e20)
        g.Edges.append(e20)

        e21 = Edge(10, 9, 1.0887225789883779)
        g.Nodes[10].add_out_edge(e21)
        g.Nodes[9].add_in_edge(e21)
        g.Edges.append(e21)

        g.distances_nodes()
        self.assertEqual(g.center_point(), 7)

    def test_allocate_agent(self):
        self.fail()

