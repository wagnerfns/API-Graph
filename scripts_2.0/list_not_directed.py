from graph_abc import AbsStrategy


class ListNotDirected(AbsStrategy):

    def directed(self):
        return(False)

    def graph_type(self):
        return(False)
