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
	
	def created_matrix(self):
		'''Create an array

		An array is created from how many vertices were generated and all are stored in a dictionary.'''
		vertex_quantity = len(self.dictionary_vertex)
		for i in range(vertex_quantity):
			list_v = []
			for i in range(vertex_quantity):

				list_v.append(0)
			self.adjacency.append(list_v)
		
	def add_vertex(self, vertex):
		'''Create a vertex

		First, check if it is a vertex and if it is not already a vertex inserted.
		If it was not inserted  then add a vertex and return True. if the vertex has already been inserted return False'''
		if isinstance(vertex, Vertex) and vertex.name not in self.dictionary_vertex:
			self.dictionary_vertex[vertex.name] = vertex
			return(True)
		else:
			return(False)

	def add_edge(self, vertex1, vertex2):
		'''Creating an edge:

		First check if it is an object, after being directed or not directed. 
		Created a list or matrix, if it is chosen an array will be created with the amount of vertices inserted (1 ... n)
		then it is necessary to enter values in that range.
		'''
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

	def eulerian(self):
		'''Verify if is Eulerian:

		First verify if is an array or adjacency list, after verify quantity number of vertex even and odd.
		If the number of vertex is equal to the number of vertex even, is eulerian.
		If the number of vertex less 2 is equal to the number of vertex even, is eulerian open.
		If none other, isn't eulerian
		'''
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
		'''Depth-First Search:

		It receives a vertex and creates a time equal to 1 and calls the _dfs function.
		It adds the vertice as gray (visited) of the time of it and searches its neighbors that are equal white (not visited) and makes a recursive call of _dfs.
		After going through all the vertices it paints each one of them in black (finalized) and adds the final time of discovery.'''
		
		global time

		time = 1
		self._dfs(vertex)

		return(True)
	
	def bfs(self, vertex):
		'''Breadth-First Search:

		It receives a vertex and pint of gray (visited) and creates a list of vertices and adds 1 to that decoberta.
		As long as the list is greater than 0, the first element of the list will be picked up and painted gray (visited) and it will search for vertices adjacent to it (white vertices).
		Finding white (unvisited) vertices will be added to the list and given a breakthrough value depending on the parent vertex.
		This will occur until all the vertices are visited.
		'''
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

	def conected(self, temp, v, visited): 
	  
		# Mark the current vertex as visited 
		visited[v] = True

		# Store the vertex to list 
		temp.append(v) 

		# Repeat for all vertices adjacent 
		# to this vertex v 
		for i in self.dictionary_vertex[v].neighbors: 
			if visited[i] == False: 
				# Update the list 
				temp = self.conected(temp, i, visited) 
		return temp 

	def connectedComponents(self):
		visited = [] 
		cc = [] 

		for i in range(len(self.dictionary_vertex)): 
			visited.append(False) 
		for v in range(len(self.dictionary_vertex)): 
			if visited[v] == False:
				temp = [] 
				cc.append(self.conected(temp, v, visited)) 
		#return cc
		return True
			
	def print_graph(self, verbose=None, dfs = None):
		''' Print all graphs:

		For print graph equal (True), print an array.
		For graph equal (False) print list adjacency.
		For print graph dfs equal (False and True).
		For print graph bfs equal (False and False)
		'''
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
