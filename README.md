# API GRAPH
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e29fdd951b1845f39e98daffe6cbf32a)](https://www.codacy.com/app/wagnerfns/API-Graph?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=wagnerfns/API-Graph&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/wagnernegrao/API-Graph.svg?branch=master)](https://travis-ci.org/wagnernegrao/API-Graph)
[![codecov](https://codecov.io/gh/wagnernegrao/API-Graph/branch/master/graph/badge.svg)](https://codecov.io/gh/wagnernegrao/API-Graph)
[![](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/download/releases/3.5.0/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This is a project at my university in the graphs discipline, the project is an graphs API, for using graphs functions using python.

This project is compatible with python3.6

## What was implemented
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
  - Topological Sorting
  - ?

## Dependencies
To install, run: ```pip install -r requirements.txt``` will be installed, pytest, unittest and coverage.

## How to use
This project creates a graph using adjacency array and adjacency list.

For creating a graph is necessary to initialize a class ```graph = Graph()```, a project can use graph directed and not directed using array or list.

Create a graph using an array is instanced ```graph = Graph(True, *)``` and graph using adjacency list is instanced ```graph = Graph(False,*)```.

You can create a graph directed and not directed. For a graph directed using an array ```graph = Graph(True, True)```, for a graph directed using a list ```graph = Graph(False, True)```, also create a graph not directed using an array ```graph = Graph(True, False)``` or list ```graph = Graph(False, False)```.

#### Creating a vertex
For create a vertex is necessary to initialize a graph, let's create a graph not directed using an array for example:

```py
  graph = Graph(True, False)
  a = Vertex(0)
  b = Vertex(1)
```

#### Creating an array and adjacency list
For create an array is necessary to have created vertex, after created the vertex, initialize a graph using ```graph.create_array()```.
Important to know: if you to use adjacency list not necessary initialize the list because when creating a graph is initialized automatically an adjacency list by default.

- Adjacency Array
```py
  graph = Graph(True, False)
  a = Vertex(0)
  b = Vertex(1)
  graph.create_array()
```

- Adjacency List
```py
  graph = Graph(True, False)
  a = Vertex(0)
  b = Vertex(1)
```

#### Creating an edge
Create an edge is necessary to have initialized a graph, use the ```graph.add_edge(a, a)``` for create an edge.

```py
graph = Graph(True, False)
a = Vertex(0)
b = Vertex(1)
graph.create_array()
graph.add_edge(a, a)
graph.add_edge(b, b)
```

## How each method works
To know how each method is working use the ```__doc__``` command to know the documentation of each method. An example of using ```print(graph.add_edg .__ doc__)```, so documentation of that method can be read via command line.

## Run test
The test will run locally.

### How to run a single unit test
To run the unit test ```pytest test/test_core.py```.

### How to run coverage
To run the coverage ```coverage run -m pytest``` this will generate a .coverage file, then run ```coverage report```.

## How contribuit

## Licence
GPLv3
