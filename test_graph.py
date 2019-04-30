Class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list() #vertices ligados a esse vertice
		self.discovery = 0
		self.finish = 0
		self.color = 'grey'
	
	def add_vertex(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v) #adiciona um vizinho ao vertice
			self.neighbors.sort() #ordena

Class Graph:
	def __init__(self, directed=None, verbose=None, quantity=None):
		self.adjacency = []
		self.directed = directed #flag para saber se eh direcioando ou nao
		self.adjacency_type = verbose # flag para saber eh lista ou matriz
		self.quantity = quantity #quantidade de vertices
		
		if(self.adjacency_type):
			for i in range(self.quantity):
				list_vertex=[]
				for i in range(self.quantity):
					list_vertex.append(0)
				self.adjacency.append(list_vertex)
		else:
			for i in range(self.quantity):
				self.adjacency.append([])
	vertices = {}
	time = 0
'''
	def add_vertex(self, vertex):
		#verifica se eh um vertice e se ja nao foi um  vertice inserido
		if isinstance(vertex, Vertex) and vertex.name not in self.adjacency:
			if(self.adjacency_type):
				for i in range(self.quantity)
					if vertex.name not in self.adjacency[i]: 
						self.vertices[vertex.name] = vertex
			return(True)
		else:
			return(False)
'''	
	def add_edge(self, vertex1, vertex2):
		if(isinstance(vertex1, Vertex)) and (isinstance(vertex2, Vertex)):
			if(directed):
				if(self.adjacency_type):
					self.adjacency[vertex1][vertex2] = 1
				else:
					self.adjacency[vertex1] = vertex2
			else:
				if(self.adjacency_type):
					self.adjacency[vertex1][vertex2] = 1
					self.adjacency[vertex2][vertex1] = 1
				else:
					self.adjacency[vertex1] = 1
					self.adjacency[vertex2] = 1
	
	def print_graph(self, verbose=None):
		if(verbose):
			for i in range(self.quantity):
				print(f'{[i]} -> {self.adjacency[i]}')
		else:
			for i in range(self.quantity):
				print(f'{[i]} -> {self.adjacency[i]}')

