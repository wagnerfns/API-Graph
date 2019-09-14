import unittest
from scripts.graph import Graph
from scripts.vertex import Vertex

"""Test."""


class TestTransitiveClosing(unittest.TestCase):
    """Create Test."""

    def test_transitive_closing_array_directed(self):
        """Test."""
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
        graph.add_edge(b, c)
        graph.add_edge(c, d)

        self.assertEqual(graph.transitive_closing(), True, msg='Teste 13')

    def test_transitive_closing_array_not_directed(self):
        """Test."""
        graph = Graph(True, False)  # matriz nao direcionada
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
        graph.add_edge(b, c)
        graph.add_edge(c, d)

        self.assertEqual(graph.transitive_closing(), False, msg='Teste 14')


if __name__ == '__main__':
    unittest.main()
