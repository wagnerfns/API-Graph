from graph_abc import AbsStrategy


class ArrayDirected(AbsStrategy):
    """Array directed"""

    def directed(self):
        return(True)

    def graph_type(self):
        return(True)
