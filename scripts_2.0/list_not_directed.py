from graph_abc import AbsStrategy


class ListNotDirected(AbsStrategy):
    """List not directed"""

    def directed(self):
        return(False)

    def graph_type(self):
        return(False)
