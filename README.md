[![Build Status](https://travis-ci.org/wagnerfns/API-Graph.svg?branch=master)](https://travis-ci.org/wagnerfns/API-Graph)
[![Coverage Status](https://coveralls.io/repos/github/wagnerfns/API-Graph/badge.svg?branch=master)](https://coveralls.io/github/wagnerfns/API-Graph?branch=master)
[![](https://img.shields.io/badge/python-3.5+-blue.svg)](https://www.python.org/download/releases/3.5.0/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


# Grafos:

This is a project in my university in the discipline of graphs, the project is an API of graphs, for using functions od graphs using python.

This project is compatible from python3.6

## what was implemented:

Currently this project has these methods of graphs:

- Directed Matrix
- Not directed Matrix
- List adjacency directed
- Search Vertex
- List adjacency not directed
- Eulerian open or closed
- Depth First Search(DFS)
- Breadth First Search(BFS)
- Connected Components
- ?

## Dependencies:

To install, run: ```pip install -r requirements.txt``` will be installed, pytest, unittest and coverage.

## How to run:
### Using the graph:
#### Creating a vertex:
#### Creating an edge:
#### Creating an array:


## How to run test:

The test will run locally.

### How to run a single unit test:

To run the unit test ```pytest test/test_core.py```.

### How to run coverage:

To run the coverage ```coverage run -m pytest``` this will generate a .coverage file, then run ```coverage report```.

## How each method works:

To know how each method is working use the ```__doc__``` command to know the documentation of each method. An example of using ```print(graph.add_edg .__ doc__)```, so documentation of that method can be read via command line.

## How contribuit:

## Licence:
GPLv3
