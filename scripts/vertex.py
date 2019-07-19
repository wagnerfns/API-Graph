class Vertex(object):
    """Create Vertex."""

    def __init__(self, n):
        """Test."""
        self.name = n
        self.neighbors = list()  # vertices ligados a esse vertice
        self.discovery = 0
        self.finish = 0
        self.distance = 9999
        self.color = 'white'

    def add_array(self, v):
        """Test."""
        if v not in self.neighbors:
            self.neighbors.append(v)  # adiciona um vizinho ao vertice
            self.neighbors.sort()  # ordena
