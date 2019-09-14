import unittest
from scripts.graph import Graph
from scripts.vertex import Vertex

"""Test."""


class TestTopologicalSorting(unittest.TestCase):
    """Create Test."""
    def test_topological_sorting_adjacency_lis_directed(self):
        """Test."""
        graph = Graph(False, True)  # list direcionada

        a = Vertex(0)
        b = Vertex(1)
        c = Vertex(2)
        d = Vertex(3)
        e = Vertex(4)
        f = Vertex(5)

        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.add_vertex(c)
        graph.add_vertex(d)
        graph.add_vertex(e)
        graph.add_vertex(f)

        graph.add_edge(f, a)
        graph.add_edge(f, c)
        graph.add_edge(c, d)
        graph.add_edge(d, b)
        graph.add_edge(e, a)
        graph.add_edge(e, b)

        self.assertEqual(graph.topological_sorting(), True, msg='Teste 1')


if __name__ == '__main__':
    unittest.main()
