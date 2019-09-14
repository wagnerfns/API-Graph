import unittest
from scripts.graph import Graph
from scripts.vertex import Vertex

"""Test."""


class TestSearch(unittest.TestCase):
    """Create Test."""

    def test_search_vertex_array_not_directed(self):
        """Test search vertex array not directed."""
        graph = Graph(True, False)
        a = Vertex(0)
        b = Vertex(1)
        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.create_array()
        graph.add_edge(a, a)
        graph.add_edge(a, b)
        self.assertEqual(graph.search_vertex(a), [0, 1], msg='Teste 1')

    def test_search_vertex_list_not_directed(self):
        """Test search vertex list not directed."""
        graph = Graph(False, False)
        a = Vertex(0)
        b = Vertex(1)
        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.add_edge(a, a)
        graph.add_edge(a, b)
        self.assertEqual(graph.search_vertex(a), [0, 1], msg='Teste 2')


if __name__ == '__main__':
    unittest.main()
