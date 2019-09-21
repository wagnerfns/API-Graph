from graphy import Graphy
from graph_directed import GraphDirected
from graph import Graph


graph = GraphDirected()

c_graph = Graph(graph)
c_graph.graph_type()


print(c_graph.adj_type)
print(c_graph.directed)
print("True")