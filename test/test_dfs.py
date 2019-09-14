import unittest
from scripts.graph import Graph
from scripts.vertex import Vertex

"""Test."""


class TestDFS(unittest.TestCase):
    """Create Test."""

    def test_dfs_list_not_directed(self):
        """Test dfs list not directed."""
        graph = Graph(False, False)  # list adjacency not directed

        a = Vertex(1)
        b = Vertex(2)
        c = Vertex(3)
        d = Vertex(4)
        e = Vertex(5)
        f = Vertex(6)
        g = Vertex(7)
        h = Vertex(8)

        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.add_vertex(c)
        graph.add_vertex(d)
        graph.add_vertex(e)
        graph.add_vertex(f)
        graph.add_vertex(g)
        graph.add_vertex(h)

        graph.add_edge(a, b)
        graph.add_edge(a, h)
        graph.add_edge(a, f)
        graph.add_edge(a, g)
        graph.add_edge(b, h)
        graph.add_edge(c, f)
        graph.add_edge(d, c)
        graph.add_edge(e, d)
        graph.add_edge(f, g)
        graph.add_edge(g, h)

        self.assertEqual(graph.dfs(e), 17, msg='Teste 11')


if __name__ == '__main__':
    unittest.main()
