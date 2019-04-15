import unittest
from grafo import Graph

class TestMethods(unittest.TestCase):

    def test_add_vertex_matrix_not_directed(self):
        graph = Graph(2)
        self.assertEqual(graph.add_vertex(0, 1), [[0,1],[1,0]], msg='Teste 1')

    def test_add_vertex_matrix_directed(self):
        graph = Graph(2, True, True)
        self.assertEqual(graph.add_vertex(0, 1, True, True), [[0,1],[0,0]], msg='Teste 2')
    
    def test_add_vertex_list_not_directed(self):
        graph = Graph(2, False, False)
        self.assertEqual(graph.add_vertex(0, 1, False, False), [[1],[0]], msg='Teste 3')

    def test_add_vertex_list_directed(self):
        graph = Graph(2, True, False)
        self.assertEqual(graph.add_vertex(0, 1, True, False), [[1],[]], msg='Teste 4')

    def test_search_vertex_matrix_not_directed(self):
        graph = Graph(2)
        graph.add_vertex(0,1)
        self.assertEqual(graph.search_vertex(0), [0,1], msg='Teste 5')
    
    def test_eulerian_true_matrix_close(self):
        graph = Graph(2)
        graph.add_vertex(0, 1)
        graph.add_vertex(0, 0)
        graph.add_vertex(1, 1)
        self.assertEqual(graph.eulerian(), True, msg="Teste 6")

    def test_eulerian_true_matrix_open(self):
        graph = Graph(6)
        graph.add_vertex(0,0)
        graph.add_vertex(0,1)
        graph.add_vertex(0,2)
        graph.add_vertex(1,1)
        graph.add_vertex(2,2)
        graph.add_vertex(3,3)
        graph.add_vertex(3,4)
        graph.add_vertex(3,5)
        graph.add_vertex(4,5)
        self.assertEqual(graph.eulerian(), True, msg="Teste 7")

    def test_eulerian_false_matrix(self):
        graph = Graph(2)
        graph.add_vertex(0, 1)
        graph.add_vertex(0, 0)
        self.assertEqual(graph.eulerian(), False, msg="Teste 8")
    
   


if __name__ == '__main__':
    unittest.main()