from graphy import Graphy


class Graph(Graphy):

    def __init__(self, strategy):
        super().__init__()
        self._strategy = strategy
        self.directed = None #self._strategy.directed()
        self.adj_type = None

    def graph_type(self):

        self.directed = self._strategy.directed()
        self.adj_type = self._strategy.adj_type()
