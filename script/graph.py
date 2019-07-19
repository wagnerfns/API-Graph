import numpy as np
from collections import defaultdict
from vertex import Vertex

class Graph:
    """Graph class."""

    """Important to know: \ and the indentation, symbolize that the next line
    is part of the line above it, this occurs because the line acquired more
    than 80 characters.
    """

    def __init__(self, verbose=None, directed=None):
        """Initialize the graph and its type."""
        self.array = []  # cria adjacency_list para adjacencia
        self.directed = directed  # flag para saber se eh direcioando ou nao
        self.adj_type = verbose  # flag para saber eh adjacency_list ou matriz
        self.adjacency_list = {}  # is a dictionary of vertex
        self.weight = {}
    time = 0

    def create_array(self):
        """Create an array.

        An array is created from how many vertices were generate and
        all are stored in a dictionary

        """
        vertex_quantity = len(self.adjacency_list)
        for i in range(vertex_quantity):
            list_v = []
            for i in range(vertex_quantity):
                list_v.append(0)

            self.array.append(list_v)

    def add_vertex(self, vertex):
        """Create a vertex.

        First, check if it is a vertex and if it is not already a vertex
        inserted. If it was not inserted  then add a vertex and return True.
        if the vertex has already been inserted return False.

        """
        if (isinstance(vertex, Vertex)):
            if (vertex.name not in self.adjacency_list):
                self.adjacency_list[vertex.name] = vertex
                return(True)
            else:
                return(False)

    def add_edge(self, vertex1, vertex2, weight=0):
        """Create an edge.

        First check if it is an object, after being directed or not directed.
        Created a list or array, if it is chosen an array will be created with
        the amount of vertices inserted (1 ... n) then it is necessary to enter
        values in that range.

        """
        self.weight[(vertex1, vertex2)] = weight
        # verify if created vertex
        if(isinstance(vertex1, Vertex)) and (isinstance(vertex2, Vertex)):
            if(self.adj_type):  # created array

                if(self.directed):  # if directed or not directed
                    self.array[vertex1.name][vertex2.name] = 1

                    self.adjacency_list[vertex1.name].add_array(vertex2.name)
                else:
                    self.array[vertex1.name][vertex2.name] = 1
                    self.array[vertex2.name][vertex1.name] = 1

                    self.adjacency_list[vertex1.name].add_array(vertex2.name)
                    self.adjacency_list[vertex2.name].add_array(vertex1.name)
                return(True)
            else:  # created list
                if(self.directed):  # if directed or not directed

                    self.adjacency_list[vertex1.name].add_array(vertex2.name)
                else:
                    self.adjacency_list[vertex1.name].add_array(vertex2.name)
                    self.adjacency_list[vertex2.name].add_array(vertex1.name)
                return(True)

    def search_vertex(self, vertex):
        """Test."""
        # print(f"Vertex: {vertex.name} - {vertex.neighbors}")
        return(vertex.neighbors)

    def eulerian(self):
        """Verify if is Eulerian.

        First verify if is an array or adjacency list, after verify quantity
        number of vertex even and odd. If the number of vertex is equal to the
        number of vertex even, is eulerian. If the number of vertex less 2 is
        equal to the number of vertex even, is eulerian open. If none other,
        isn't eulerian.

        """
        eulerian = 0
        if(self.adj_type):
            for i in range(len(self.adjacency_list)):
                count = 0
                for j in range(len(self.adjacency_list)):
                    if(self.array[i][j] == 1):
                        count += 1
                if(count % 2 == 0):
                    eulerian += 1
        else:
            for i in range(len(self.adjacency_list)):
                count = len(self.adjacency_list[i].neighbors)
                if(count % 2 == 0):
                    eulerian += 1

        if(len(self.adjacency_list) == eulerian):
            prt = "Is Eulerian"
            print(prt)
            return(prt)
        elif((len(self.adjacency_list) - 2) == eulerian):
            prt = "Eulerian open"
            print(prt)
            return(prt)
        else:
            prt = "Not is eulerian"
            print(prt)
            return(prt)

    def _dfs(self, vertex):
        """Test."""
        global time
        vertex.color = 'gray'
        vertex.discovery = time
        time += 1

        for i in vertex.neighbors:
            if(self.adjacency_list[i].color == 'white'):
                self._dfs(self.adjacency_list[i])

        vertex.color = 'black'
        vertex.finish = time
        time += 1

    def dfs(self, vertex, timing=1):
        """Depth-First Search.

        It receives a vertex and creates a time equal to 1 and calls the _dfs
        function. It adds the vertice as gray (visited) of the time of it and
        searches its neighbors that are equal white (not visited) and makes a
        recursive call of _dfs. After going through all the vertices it paints
        each one of them in black (finalized) and adds the final time of
        discovery.

        """
        global time
        time = timing
        self._dfs(vertex)
        return(time)

    def bfs(self, vertex):
        """Breadth-First Search.

        It receives a vertex and pint of gray (visited) and creates a list of
        vertices and adds 1 to that decoberta. As long as the list is greater
        than 0, the first element of the list will be picked up and painted
        gray (visited) and it will search for vertices adjacent to it
        (white vertices). Finding white (unvisited) vertices will be added to
        the list and given a breakthrough value depending on the parent vertex.
        This will occur until all the vertices are visited.
        """
        queue = list()
        vertex.distance = 0
        vertex.color = 'gray'

        for v in vertex.neighbors:
            self.adjacency_list[v].distance = vertex.distance + 1
            queue.append(v)

        while(len(queue) > 0):
            u = queue.pop(0)
            node_u = self.adjacency_list[u]
            node_u.color = 'gray'  # paint gray

            for v in node_u.neighbors:
                node_v = self.adjacency_list[v]
                if(node_v.color == 'white'):
                    queue.append(v)
                    if(node_v.distance > node_u.distance + 1):
                        node_v.distance = node_u.distance + 1
        return(True)

    def conected(self, temp, index, visited):
        """Verify if is conected.

        You will receive a temporary list, index, and list of the visited.

        The index will tell which vertex value is being visited and mark it as
        visited and store the vertex in the temporary list. This will be
        repeated for all vertices adjacent to the vertex of the index.

        For each vertex adjacent to the vertex [index] and if it is not visited
        then checks if it is connected, this recursive call will occur until
        the list of vertices visited is set to True.
        """
        # Mark the current vertex as visited
        visited[index] = True

        # Store the vertex to list
        temp.append(index)

        # Repeat for all vertices adjacent
        # to this vertex index
        for i in self.adjacency_list[index].neighbors:
            if (visited[i] is False):
                # Update the list
                temp = self.conected(temp, i, visited)
        return temp

    def connected_components(self):
        """Verify if is Connected Components.

        Creates a list of visited vertices and declares all false. As long as
        there are unvisited elements will search for new connected element,
        for each connected component will be added in a list of connected.
        """
        visited = []
        connected_component = []

        for i in range(len(self.adjacency_list)):
            visited.append(False)
        for v in range(len(self.adjacency_list)):
            if not visited[v]:
                temp = []
                connected_component.append(self.conected(temp, v, visited))
        # print(f"connected_component: {connected_component}")
        return (True)

    def transitive_closing(self):
        """Array transitive closing.

        makes a copy of the matrix and multiplies the matrices to the vertices
        quantity, and for each iteration True it adds 1 to that point in the
        copy matrix and part to a new iteration.
        """
        if(self.directed):
            size = len(self.adjacency_list)
            array_transitive = np.copy(self.array)
            for y in range(size):
                for i in range(size):
                    for j in range(size):
                        for l in range(size):
                            if ((self.array[i][l] == 1) and
                               (array_transitive[l][j] == 1)):

                                array_transitive[i][j] = 1

            # print("Array")
            # for i in range(size):
            #     print(self.array[i])
            # print("Array transitive closing")
            # for i in range(size):
            #    print(array_transitive[i])
            return(True)
        else:
            return(False)

    def algorithm_warshall(self):
        """Array algorithm warshall.

        first, verify if directed or not directed. After is created a copy of
        the array. While traversing the copy matrix, a check is made if the row
        and column have 1 and at that specific point has zero is added 1.
        """
        if(self.directed):
            size = len(self.adjacency_list)
            array_warshall = np.copy(self.array)

            for k in range(size):
                for i in range(size):
                    for j in range(size):
                        if ((array_warshall[i][j] == 0) and
                           (array_warshall[i][k] == 1) and
                           (array_warshall[k][j] == 1)):

                            array_warshall[i][j] = 1

            print("Array")
            for i in range(size):
                print(self.array[i])
            print("The transitive closure of the digraph")
            for i in range(size):
                print(array_warshall[i])
            return(True)
        else:
            return(False)

    def topological_sorting(self):
        """Test."""
        list_not_origin = []
        list_origin = []

        for i in range(len(self.adjacency_list)):
            for j in range(len(self.adjacency_list)):
                if i in self.adjacency_list[j].neighbors:
                    list_not_origin.append(i)
                else:
                    list_origin.append(i)

        list_not_origin = sorted(set(list_not_origin))
        list_origin = sorted(set(list_origin))

        for k in range(len(list_origin)):
            if k in list_not_origin:
                list_origin.remove(k)

        time = 1

        for i in range(len(list_origin)):
            time = (self.dfs(self.adjacency_list[list_origin[i]], time))

        test = {}
        for key in sorted(list(self.adjacency_list.keys())):
            test[self.adjacency_list[key].finish] = key

        for i in sorted(list(test.keys()), reverse=True):
         print(f"vertex: {test[i]} - {i}")
        return(True)

    def SCCUtil(self, u, low, disc, stackMember, st):

        # Initialize discovery time and low value

        global time
        disc[u] = time
        low[u] = time
        time += 1
        stackMember[u] = True
        st.append(u)

        # Go through all vertices adjacent to this
        for v in self.adjacency_list[u].neighbors:

            # If v is not visited yet, then recur for it
            if disc[v] == -1:

                self.SCCUtil(v, low, disc, stackMember, st)

                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                # Case 1 (per above discussion on Disc and Low value)
                low[u] = min(low[u], low[v])

            elif stackMember[v] == True:

                '''Update low value of 'u' only if 'v' is still in stack
                (i.e. it's a back edge, not cross edge).
                Case 2 (per above discussion on Disc and Low value) '''
                low[u] = min(low[u], disc[v])

        # head node found, pop the stack and print an SCC
        w = -1 #To store stack extracted vertices
        if low[u] == disc[u]:
            while w != u:
                w = st.pop()
                print(w)
                stackMember[w] = False

            print("--")

    #The function to do DFS traversal.
    # It uses recursive SCCUtil()
    def SCC(self):
        for i in range(len(self.adjacency_list)):
                        print(f'{[i]} -> {self.array[i]}')
        # Mark all the vertices as not visited
        # and Initialize parent and visited,
        # and ap(articulation point) arrays
        disc = [-1] * len(self.adjacency_list)
        low = [-1] * len(self.adjacency_list)
        stackMember = [False] * len(self.adjacency_list)
        st =[]

        global time
        time = 0
        # Call the recursive helper function
        # to find articulation points
        # in DFS tree rooted with vertex 'i'
        for i in range(len(self.adjacency_list)):
            if disc[i] == -1:
                self.SCCUtil(i, low, disc, stackMember, st)
        return(True)

# graph = Graph(True, True)  # matriz direcionada
# graph = Graph(True, False)  # matriz nao direcionada
# graph = Graph(False, False)  # list adjacency not directed
# graph = Graph(False, True)  # list adjacency directed


