import unittest
from scripts.graph import Graph
from scripts.vertex import Vertex

"""Test."""


class TestWarshall(unittest.TestCase):
    """Create Test."""
    def test_algorithm_warshall_array_directed(self):
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

        graph.add_edge(a, d)
        graph.add_edge(b, a)
        graph.add_edge(b, c)
        graph.add_edge(c, a)
        graph.add_edge(c, d)
        graph.add_edge(d, c)

        self.assertEqual(graph.algorithm_warshall(), True, msg='Test 1')

    def test_algorithm_warshall_array_not_directed(self):
        """Test."""
        graph = Graph(True, False)  # matriz not direcionada

        a = Vertex(0)
        b = Vertex(1)
        c = Vertex(2)
        d = Vertex(3)
        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.add_vertex(c)
        graph.add_vertex(d)

        graph.create_array()

        graph.add_edge(a, d)
        graph.add_edge(b, a)
        graph.add_edge(b, c)
        graph.add_edge(c, a)
        graph.add_edge(c, d)
        graph.add_edge(d, c)

        self.assertEqual(graph.algorithm_warshall(), False, msg='Test 2')


if __name__ == '__main__':
    unittest.main()
