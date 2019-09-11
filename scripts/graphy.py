
class Graphy:
    """Graphy class."""

    """
    This is superclass the graph.
    These arguments are privet.
    It is implemented by default,  array, adjacency list, and weight.
    Is used the property to use getter and setter.
    """

    def __init__(self):
        self.__array = []  # cria adjacency_list para adjacencia
        self.__adjacency_list = {}  # is a dictionary of vertex
        self.__weight = {}

    @property
    def array(self):
        return (self.__array)

    @array.setter
    def array(self, value):
        self.__array.append(value)

    @property
    def adjacency_list(self):
        return(self.__adjacency_list)

    @adjacency_list.setter
    def adjacency_list(self, value):
        self.__adjacency_list.append(value)

    @property
    def weight(self):
        return(self.__weight)

    @weight.setter
    def weight(self, value):
        self.__weight = value
