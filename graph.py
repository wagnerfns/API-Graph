class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list() #vertices ligados a esse vertice
		self.discovery = 0
		self.finish = 0
		self.distance = 9999
		self.color = 'white'
	
	def add_adjacency(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v) #adiciona um vizinho ao vertice
			self.neighbors.sort() #ordena
	
	#def search_vertex(self, index):
	#	print(f"Vertex: {index} - {self.dictionary_vertex}")

class Graph:
	def __init__(self, verbose=None, directed=None):
		self.adjacency = [] # cria lista para adjacencia
		self.directed = directed #flag para saber se eh direcioando ou nao
		self.adjacency_type = verbose # flag para saber eh lista ou matriz
		self.dictionary_vertex = {}
		
		
	time = 0
	
	'''
	If choice is list created a list or a matrix
	'''
	def created_matrix(self):
		vertex_quantity = len(self.dictionary_vertex)
		for i in range(vertex_quantity):
			list_v = []
			for i in range(vertex_quantity):

				list_v.append(0)
			self.adjacency.append(list_v)
	'''
	'''		
	def add_vertex(self, vertex):
		#verifica se eh um vertice e se ja nao foi um  vertice inserido
		if isinstance(vertex, Vertex) and vertex.name not in self.dictionary_vertex:
			self.dictionary_vertex[vertex.name] = vertex

			return(True)
		else: # return false if vertex insured
			return(False)

	
	'''
	First verify if is a object after if is directed and 
	created a list or matrix, if matrix created a matrix with size vertex
	'''
	def add_edge(self, vertex1, vertex2):
		if(isinstance(vertex1, Vertex)) and (isinstance(vertex2, Vertex)): # verify if created vertex
			if(self.adjacency_type):# created matrix
								
				if(self.directed): #if directed or not directed
					self.adjacency[vertex1.name][vertex2.name] = 1
				else:
					self.adjacency[vertex1.name][vertex2.name] = 1
					self.adjacency[vertex2.name][vertex1.name] = 1
				return(True)
			else: # created list
				if(self.directed): #if directed or not directed
					self.dictionary_vertex[vertex1.name].add_adjacency(vertex2.name)
				else:
					self.dictionary_vertex[vertex1.name].add_adjacency(vertex2.name)
					self.dictionary_vertex[vertex2.name].add_adjacency(vertex1.name)
				return(True)

	'''
	First verify if is, matriz or adjacency list, after verify quantity number of vertex even and odd.
	if the number of vertex is equal to the number of vertex even, is eulerian closed,
	if the number of vertex less 2 is equal to the number of vertex even, is eulerian open,  
	if none other, isn't eulerian
	'''
	def eulerian(self):
		eulerian = 0
		if(self.adjacency_type):
			for i in range(len(self.dictionary_vertex)):
				count = 0
				for j in range(len(self.dictionary_vertex)):
					if(self.adjacency[i][j] == 1):
						count += 1
				if(count%2 == 0):
					eulerian += 1
		else:
			for i in range(len(self.dictionary_vertex)):
				count = len(self.dictionary_vertex[i].neighbors)
				if(count%2 == 0):
					eulerian += 1

		if(len(self.dictionary_vertex) == eulerian):
			prt = "Is Eulerian"
			print(prt)
			return(prt)
		elif((len(self.dictionary_vertex) - 2) == eulerian):
			prt = "Eulerian open"
			print(prt)
			return(prt)
		else:
			prt = "Not is eulerian"
			print(prt)
			return(prt)

	'''
	'''
	def _dfs(self, vertex):
		global time
		vertex.color = 'gray'
		vertex.discovery = time
		time += 1

		for i in vertex.neighbors:
			if(self.dictionary_vertex[i].color == 'white'):
				self._dfs(self.dictionary_vertex[i])

		vertex.color = 'black'
		vertex.finish = time
		time += 1

	def dfs(self, vertex):
		global time

		time = 1
		self._dfs(vertex)

		return(True)
	def bfs(self, vertex):
		queue = list()
		vertex.distance = 0
		vertex.color = 'gray'

		for v in vertex.neighbors:
			self.dictionary_vertex[v].distance = vertex.distance + 1
			queue.append(v)

		while(len(queue) > 0):
			u = queue.pop(0)
			node_u = self.dictionary_vertex[u]
			node_u.color = 'gray' #paint black

			for v in node_u.neighbors:
				node_v = self.dictionary_vertex[v]
				if(node_v.color == 'white'):
					queue.append(v)
					if(node_v.distance > node_u.distance + 1):
						node_v.distance = node_u.distance + 1
		return(True)
			
	'''
	If print graph equal (True), print a matrix, if graph equal (False) print list adjacency
	if print way graph dfs equal (False and True)
	if print way graph bfs equal (False and False)
	'''

	def print_graph(self, verbose=None, dfs = None):
		if(verbose):
			for i in range(len(self.dictionary_vertex)):
				print(f'{[i]} -> {self.adjacency[i]}')
		elif(verbose == False and dfs == None):
			for key in sorted(list(self.dictionary_vertex.keys())):
					print(f"{key} - {self.dictionary_vertex[key].neighbors}")
		if(dfs == True):
			for key in sorted(list(self.dictionary_vertex.keys())):
				print(f"{key} - {self.dictionary_vertex[key].neighbors} - {self.dictionary_vertex[key].discovery}")
		else:
			for key in sorted(list(self.dictionary_vertex.keys())):
				print(f"{key} - {self.dictionary_vertex[key].neighbors} - {self.dictionary_vertex[key].distance}")


#graph = Graph(True, True)  # matriz direcionada
#graph = Graph(True, False) # matriz nao direcionada
#graph = Graph(False, False) # list adjacency not directed
#graph = Graph(False, True)  # list adjacency directed
