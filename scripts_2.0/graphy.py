
class Graphy:
    """Graphy class."""

    """
    This is superclass the graph.
    These arguments are privet.
    It is implemented by default,  array, adjacency list, and weight.
    Is used the property to use getter and setter.
    """

    def __init__(self):
        self._array = []  # cria adjacency_list para adjacencia
        self._adjacency_list = {}  # is a dictionary of vertex
        self._weight = {}

    @property
    def array(self):
        return (self._array)

    @array.setter
    def array(self, value):
        self._array.append(value)

    @property
    def adjacency_list(self):
        return(self._adjacency_list)

    @adjacency_list.setter
    def adjacency_list(self, value):
        self._adjacency_list.append(value)

    @property
    def weight(self):
        return(self._weight)

    @weight.setter
    def weight(self, value):
        self._weight = value
