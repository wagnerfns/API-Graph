import unittest
from scripts.graph import Graph
from scripts.vertex import Vertex

"""Test."""


class TestBFS(unittest.TestCase):
    """Create Test."""

    def test_bfs_list_not_directed(self):
        """Test bfs list not directed."""
        graph = Graph(False, False)  # list adjacency not directed

        a = Vertex(1)
        b = Vertex(2)
        c = Vertex(3)
        d = Vertex(4)
        e = Vertex(5)
        f = Vertex(6)

        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.add_vertex(c)
        graph.add_vertex(d)
        graph.add_vertex(e)
        graph.add_vertex(f)

        graph.add_edge(a, b)
        graph.add_edge(a, c)
        graph.add_edge(b, d)
        graph.add_edge(c, d)
        graph.add_edge(c, e)
        graph.add_edge(d, c)
        graph.add_edge(d, e)
        graph.add_edge(d, f)
        graph.add_edge(e, c)
        graph.add_edge(e, d)
        graph.add_edge(e, f)
        graph.add_edge(f, e)
        graph.add_edge(f, d)

        self.assertEqual(graph.bfs(a), True, msg='Teste 1')


if __name__ == '__main__':
    unittest.main()
