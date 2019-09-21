from graph_abc import AbsStrategy


class ListDirected(AbsStrategy):
    """List directed"""

    def directed(self):
        return(True)

    def graph_type(self):
        return(False)
