import unittest
from grafo import Graph

class TestMethods(unittest.TestCase):

    def test_add_vertex_matrix_not_directed(self):
        graph = Graph(2)
        self.assertEqual(graph.add_vertex(0, 1), [[0,1],[1,0]], msg='Teste 1')

    def test_search_vertex_matrix_not_directed(self):
        graph = Graph(2)
        graph.add_vertex(0,1)
        self.assertEqual(graph.search_vertex(0), [0,1], msg='Teste 2')
    
    def test_eulerian_true_matrix(self):
        graph = Graph(2)
        graph.add_vertex(0, 1)
        graph.add_vertex(0, 0)
        graph.add_vertex(1, 1)

        self.assertEqual(graph.eulerian(), True, msg="Teste 3")

    def test_eulerian_false_matrix(self):
        graph = Graph(2)
        graph.add_vertex(0, 1)
        graph.add_vertex(0, 0)

        self.assertEqual(graph.eulerian(), False, msg="Teste 4")

if __name__ == '__main__':
    unittest.main()