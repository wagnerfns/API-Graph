import unittest
from scripts.graph import Graph
from scripts.vertex import Vertex

"""Test."""


class TestArray(unittest.TestCase):
    """Create Test."""

    def test_add_vertex_array_not_directed(self):
        """Test add vertex array not directed."""
        graph = Graph(True, False)
        a = Vertex(0)
        b = Vertex(1)
        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.create_array()
        graph.add_edge(a, a)
        graph.add_edge(b, b)
        self.assertEqual(graph.add_edge(a, b), True, msg='Teste 1')

    def test_add_vertex_array_directed(self):
        """Test add vertex array directed."""
        graph = Graph(True, True)
        a = Vertex(0)
        b = Vertex(1)
        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.create_array()
        graph.add_edge(a, a)
        graph.add_edge(b, b)
        self.assertEqual(graph.add_edge(a, b), True, msg='Teste 2')


if __name__ == '__main__':
    unittest.main()
