import unittest
from test_graph import Graph
from test_graph import Vertex


class TestMethods(unittest.TestCase):

	def test_add_vertex_matrix_not_directed(self):
		graph = Graph(True, False)
		a = Vertex(0)
		b = Vertex(1)
		graph.add_vertex(a)
		graph.add_vertex(b)
		graph.created_matrix()
		graph.add_edge(a, a)
		graph.add_edge(b, b)
		self.assertEqual(graph.add_edge(a, b), True, msg='Teste 1')
	
	def test_add_vertex_matrix_directed(self):
		graph = Graph(True, True)
		a = Vertex(0)
		b = Vertex(1)
		graph.add_vertex(a)
		graph.add_vertex(b)
		graph.created_matrix()
		graph.add_edge(a, a)
		graph.add_edge(b, b)
		self.assertEqual(graph.add_edge(a, b), True, msg='Teste 2')

	def test_add_vertex_list_not_directed(self):
		graph = Graph(False, False)
		a = Vertex(0)
		b = Vertex(1)
		graph.add_vertex(a)
		graph.add_vertex(b)
		graph.add_edge(a, a)
		graph.add_edge(b, b)
		self.assertEqual(graph.add_edge(a, b), True, msg='Teste 3')

	def test_add_vertex_list_directed(self):
		graph = Graph(False, True)
		a = Vertex(0)
		b = Vertex(1)
		graph.add_vertex(a)
		graph.add_vertex(b)
		graph.add_edge(a, a)
		graph.add_edge(b, b)
		self.assertEqual(graph.add_edge(a, b), True, msg='Teste 4')


'''
def test_eulerian_true_matrix_close(self):
def test_eulerian_true_matrix_open(self):
def test_eulerian_false_matrix(self):'''