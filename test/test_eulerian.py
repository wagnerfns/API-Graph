import unittest
from scripts.graph import Graph
from scripts.vertex import Vertex


class TestEulerian(unittest.TestCase):
    """Create Test."""

    def test_eulerian_array(self):
        """Test eulerian array."""
        graph = Graph(True, False)
        a = Vertex(0)
        b = Vertex(1)
        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.create_array()
        graph.add_edge(a, a)
        graph.add_edge(b, b)
        graph.add_edge(a, b)
        self.assertEqual(graph.eulerian(), "Is Eulerian", msg='Teste 1')

    def test_eulerian_array_open(self):
        """Test eulerian array open."""
        graph = Graph(True, False)
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
        graph.create_array()
        graph.add_edge(a, a)
        graph.add_edge(b, b)
        graph.add_edge(c, c)
        graph.add_edge(d, d)
        graph.add_edge(a, b)
        graph.add_edge(a, c)
        graph.add_edge(d, e)
        graph.add_edge(d, f)
        graph.add_edge(e, f)
        self.assertEqual(graph.eulerian(), "Eulerian open", msg='Teste 2')

    def test_not_eulerian_array(self):
        """Test not eulerian array."""
        graph = Graph(True, False)
        a = Vertex(0)
        b = Vertex(1)
        graph.add_vertex(a)
        graph.add_vertex(b)

        graph.create_array()

        graph.add_edge(a, a)
        graph.add_edge(a, b)

        self.assertEqual(graph.eulerian(), "Not is eulerian", msg='Teste 3')

if __name__ == '__main__':
    unittest.main()
