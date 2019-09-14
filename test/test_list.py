import unittest
from scripts.graph import Graph
from scripts.vertex import Vertex

"""Test."""


class TestList(unittest.TestCase):
    """Create Test."""

    def test_add_vertex_list_directed(self):
        """Test add vertex list directed."""
        graph = Graph(False, True)
        a = Vertex(0)
        b = Vertex(1)
        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.add_edge(a, a)
        graph.add_edge(b, b)
        self.assertEqual(graph.add_edge(a, b), True, msg='Teste 1')

    def test_add_vertex_list_not_directed(self):
        """Test add vertex list not directed."""
        graph = Graph(False, False)
        a = Vertex(0)
        b = Vertex(1)
        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.add_edge(a, a)
        graph.add_edge(b, b)
        self.assertEqual(graph.add_edge(a, b), True, msg='Teste 2')


if __name__ == '__main__':
    unittest.main()
