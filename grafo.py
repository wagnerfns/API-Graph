class Graph():
    
    '''
    The graph per default is not directed and is matrix.

    other settings:

    1 - directed: True and verbose: True, is a matrix directed

    2 - directed: False and verbose: False, is a list not directed

    3 - directed: True and verbose: False, is a list directed

    '''
    def __init__(self, vertex_quantity, directed=False, verbose=True):
        self.adjacency = [] # created a list for adjacency
        self.vertex_quantity = vertex_quantity
        self.directed = directed    
        self.adjacency_type = verbose
        
        if(self.adjacency_type): # if verbose false create a list, if true creat a matrix
            for i in range(vertex_quantity):
                list_v = []
                for i in range(vertex_quantity):
                    list_v.append(0)
                self.adjacency.append(list_v)
        else: #create list
            for i in range(vertex_quantity):
                self.adjacency.append([])

    def add_vertex(self, vertex1, vertex2, directed=False ,verbose=True):
        
        if(self.directed == directed == True): #check if is directed
            
            if(self.adjacency_type == verbose == True): #check if is matrix
                self.adjacency[vertex1][vertex2] = 1

            elif(self.adjacency_type == verbose == False): #check if is list
                self.adjacency[vertex1].append(vertex2) 
        else:
            if(self.adjacency_type == verbose == True): #check if is matrix
                self.adjacency[vertex1][vertex2] = 1
                self.adjacency[vertex2][vertex1] = 1

            elif(self.adjacency_type == verbose == False): #check if is list
                self.adjacency[vertex1].append(vertex2)
                self.adjacency[vertex2].append(vertex1)

        return(self.adjacency)
        
    def search_vertex(self, index):
        print(f"vertex: {index} - {self.adjacency[index]}")    
        return(self.adjacency[index])

    def print_graph(self, verbose=True):
        if(self.adjacency_type == verbose == True): #matrix   
            
            index = []
            for i in range(self.vertex_quantity): #print index matrix
                index.append(i)
            print('\t',index)     

            for i in range(self.vertex_quantity): #print matriz for line
                print(f'{[i]}\t {self.adjacency[i]}')
        else: #list
            for i in range(self.vertex_quantity):
                print(f"[{i}] -> {self.adjacency[i]}")

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
            print("E euleriano")
            return(True)
        else:
            print("Nao e euleriano")
            return(False)


graph = Graph(2)
graph.add_vertex(0, 1)
graph.add_vertex(0, 0)
graph.add_vertex(1, 1)

graph.eulerian()

graph.print_graph()

