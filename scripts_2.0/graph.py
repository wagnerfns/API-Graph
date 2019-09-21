from graphy import Graphy


class Graph(Graphy):

    def __init__(self, strategy):
        super().__init__()
        self._strategy = strategy
        self.directed = None
        self.graph_type = None

    def initialize_graph(self):

        self.directed = self._strategy.directed()
        self.graph_type = self._strategy.graph_type()
