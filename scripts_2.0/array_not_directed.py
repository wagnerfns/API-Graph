from graph_abc import AbsStrategy


class ArrayNotDirected(AbsStrategy):
    """Array not directed"""

    def directed(self):
        return(False)

    def graph_type(self):
        return(True)
