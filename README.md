[![Build Status](https://travis-ci.org/wagnerfns/API-Graph.svg?branch=master)](https://travis-ci.org/wagnerfns/API-Graph)
[![Coverage Status](https://coveralls.io/repos/github/wagnerfns/API-Graph/badge.svg?branch=master)](https://coveralls.io/github/wagnerfns/API-Graph?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e29fdd951b1845f39e98daffe6cbf32a)](https://www.codacy.com/app/wagnerfns/API-Graph?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=wagnerfns/API-Graph&amp;utm_campaign=Badge_Grade)
[![](https://img.shields.io/badge/python-3.5+-blue.svg)](https://www.python.org/download/releases/3.5.0/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


# API GRAPH
This is a project at my university in the graphs discipline, the project is an graphs API, for using graphs functions using python.

This project is compatible with python3.6

## what was implemented:
Currently, this project has these graphs methods:

- Directed Matrix
- Not directed Matrix
- List adjacency directed
- Search Vertex
- List adjacency not directed
- Eulerian open or closed
- Depth First Search (DFS)
- Breadth First Search (BFS)
- Connected Components
- Transitive Closing
- Warshall Algorithm: Transitive Closure
- ?

## Dependencies:
To install, run: ```pip install -r requirements.txt``` will be installed, pytest, unittest and coverage.

## How to use:
This project creates a graph using adjacency array and adjacency list.

For creating a graph is necessary to initialize a class ```graph = Graph()```, a project can use graph directed and not directed using array or list.

Create a graph using an array is instanced ```graph = Graph(True, *)``` and graph using adjacency list is instanced ```graph = Graph(False,*)```.


For creating a graph directed and not directed,

using array for graph directed is instanced  and for creating graph not directed


For graph directed and not directed use:

Create a graph directed using array, ```graph = Graph(True, True)```
Create a graph not directed using array, ```graph = Graph(True, False)```

Create a graph directed using adjacency list, ```graph = Graph(False, True)```
Create a graph not directed using adjacency list, ```graph = Graph(False, False)```


# graph = Graph(True, True)  # matriz direcionada
# graph = Graph(True, False)  # matriz nao direcionada
# graph = Graph(False, False)  # list adjacency not directed
# graph = Graph(False, True)  # list adjacency directed

#### Creating a vertex:
```a = Vertex(0)
   b = Vertex(1)
```

#### Creating an array and adjacency list:
```
graph.create_array()
```

#### Creating an edge:
```
graph.add_edge(a, a)
graph.add_edge(b, b)
```

## How each method works:
To know how each method is working use the ```__doc__``` command to know the documentation of each method. An example of using ```print(graph.add_edg .__ doc__)```, so documentation of that method can be read via command line.

## How to run test:
The test will run locally.

### How to run a single unit test:
To run the unit test ```pytest test/test_core.py```.

### How to run coverage:
To run the coverage ```coverage run -m pytest``` this will generate a .coverage file, then run ```coverage report```.

## How contribuit:

## Licence:
GPLv3
