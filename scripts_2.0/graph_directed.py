from graph_abc import AbsStrategy


class GraphDirected(AbsStrategy):

    def directed(self):
        return(True)

    def adj_type(self):
        return(True)
