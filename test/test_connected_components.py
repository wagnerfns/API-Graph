import unittest
from scripts.graph import Graph
from scripts.vertex import Vertex

"""Test."""


class TestConnectedComponents(unittest.TestCase):
    """Create Test."""

    def test_connected_components_list_adjacency_not_directed(self):
        """Test connected components list adjacency not directed."""
        graph = Graph(False, False)  # list adjacency not directed
        # Create a graph given in the above diagram
        # 5 vertices numbered from 0 to 4

        a = Vertex(0)
        b = Vertex(1)
        c = Vertex(2)
        d = Vertex(3)
        e = Vertex(4)

        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.add_vertex(c)
        graph.add_vertex(d)
        graph.add_vertex(e)

        graph.add_edge(a, b)
        graph.add_edge(c, d)
        graph.add_edge(d, e)

        self.assertEqual(graph.connected_components(), True, msg='Teste 1')


if __name__ == '__main__':
    unittest.main()
