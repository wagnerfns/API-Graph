from array_directed import ArrayDirected
from array_not_directed import ArrayNotDirected

from graph import Graph


graph1 = ArrayDirected()

c_graph = Graph(graph1)
c_graph.initialize_graph()



print(c_graph.directed)
print(c_graph.graph_type)
print("--/-/-/-/-/-/")



graph2 = ArrayNotDirected()

c_graph2 = Graph(graph2)
c_graph2.initialize_graph()


print(c_graph2.directed)
print(c_graph2.graph_type)
print("--/-/-/-/-/-/")