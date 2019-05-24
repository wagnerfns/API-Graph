"""Test."""

import unittest
from graph import Graph
from graph import Vertex

"""Test."""


class TestMethods(unittest.TestCase):
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

    def test_add_vertex_list_not_directed(self):
        """Test add vertex list not directed."""
        graph = Graph(False, False)
        a = Vertex(0)
        b = Vertex(1)
        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.add_edge(a, a)
        graph.add_edge(b, b)
        self.assertEqual(graph.add_edge(a, b), True, msg='Teste 3')

    def test_add_vertex_list_directed(self):
        """Test add vertex list directed."""
        graph = Graph(False, True)
        a = Vertex(0)
        b = Vertex(1)
        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.add_edge(a, a)
        graph.add_edge(b, b)
        self.assertEqual(graph.add_edge(a, b), True, msg='Teste 4')

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
        self.assertEqual(graph.search_vertex(a), [0, 1], msg='Teste 5')

    def test_search_vertex_list_not_directed(self):
        """Test search vertex list not directed."""
        graph = Graph(False, False)
        a = Vertex(0)
        b = Vertex(1)
        graph.add_vertex(a)
        graph.add_vertex(b)
        graph.add_edge(a, a)
        graph.add_edge(a, b)
        self.assertEqual(graph.search_vertex(a), [0, 1], msg='Teste 6')

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
        self.assertEqual(graph.eulerian(), "Is Eulerian", msg='Teste 7')

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
        self.assertEqual(graph.eulerian(), "Eulerian open", msg='Teste 8')

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

        self.assertEqual(graph.eulerian(), "Not is eulerian", msg='Teste 9')

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

        self.assertEqual(graph.bfs(a), True, msg='Teste 10')

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

        self.assertEqual(graph.dfs(e), True, msg='Teste 11')

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

        self.assertEqual(graph.connected_components(), True, msg='Teste 12')

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


if __name__ == '__main__':
    unittest.main()
