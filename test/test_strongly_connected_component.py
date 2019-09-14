import unittest
from scripts.graph import Graph
from scripts.vertex import Vertex

"""Test."""


class TestStronglyConnectedComponent(unittest.TestCase):
    """Create Test."""
    def test_strongly_connected_component_arry_directed(self):
        graph = Graph(True, True)  # matriz direcionada

        a = Vertex(0)
        b = Vertex(1)
        c = Vertex(2)
        d = Vertex(3)

        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.add_vertex(c)
        graph.add_vertex(d)

        graph.create_array()

        graph.add_edge(a, b)
        graph.add_edge(b, a)
        graph.add_edge(b, c)
        graph.add_edge(c, d)
        graph.add_edge(d, c)

        self.assertEqual(graph.SCC(), True, msg='Teste 1')


if __name__ == '__main__':
    unittest.main()
