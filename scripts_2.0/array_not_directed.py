from graph_abc import AbsStrategy


class ArrayNotDirected(AbsStrategy):

    def directed(self):
        return(False)

    def graph_type(self):
        return(True)
