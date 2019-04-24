
class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()
        self.discovery = 0
        self.finish = 0
        self.color = 'black'

    def add_neighbor(self, v):
        nset = set(self.neighbors)
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    vertices = {}
    time = 0
	
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbor(v)
            self.vertices[v].add_neighbor(u)
            return True
        else:
            return False
            
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + " " + str(self.vertices[key].discovery))

    def _dfs(self, vertex):
        global time
        vertex.color = 'red'
        vertex.discovery = time
        time += 1

        for v in vertex.neighbors:
       
            if self.vertices[v].color == 'black':
                self._dfs(self.vertices[v])
        
        vertex.color = 'blue'
        vertex.finish = time
        time += 1
    
    def dfs(self, vertex):
        global time

        time = 1
        self._dfs(vertex)


    def eulerian(self): #check if is eulerian
        eulerian = 0


        for i in range(self.vertex_quantity):
            count = 0
            for j in range(self.vertex_quantity):
                if(self.adjacency[i][j] == 1):
                    count += 1
            if(count%2 == 0):
                eulerian += 1
        if(self.vertex_quantity == eulerian):
            print("Euleriano fechado")
            return(True)
        elif((self.vertex_quantity - 2) == eulerian):
            print("Euleriano aberto")
            return(True)
        else:
            print("Nao e euleriano")
            return(False)


g = Graph()
# print(str(len(g.vertices)))

a = Vertex('1')
b = Vertex('2')
e = Vertex('5') 


g.add_vertex(a)
g.add_vertex(b)

g.add_vertex(e)


for i in range(ord('1'), ord('9')):
	g.add_vertex(Vertex(chr(i)))


edges = ['54', '43', '36', '61', '67', '71', '78', '82', '81', '16', '17', '18', '12', '21', '28']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])

g.dfs(e)
g.print_graph()