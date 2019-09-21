from graph_abc import AbsStrategy


class ListDirected(AbsStrategy):

    def directed(self):
        return(True)

    def graph_type(self):
        return(False)
