[![Build Status](https://travis-ci.org/wagnerfns/Grafos.svg?branch=master)](https://travis-ci.org/wagnerfns/Grafos)
[![Coverage Status](https://coveralls.io/repos/github/wagnerfns/Grafos/badge.svg?branch=master)](https://coveralls.io/github/wagnerfns/Grafos?branch=master)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


# Grafos

This is a project in my university in the discipline of graphs, the project is an API of graphs, for using functions od graphs using python.

This project is compatible from python3.6

## what was implemented

Currently this project has these methods of graphs:

- Matrix
- Directed Matrix
- Not directed Matrix
- List adjacency
- List adjacency directed
- List adjacency not directed
- Eulerian open or closed
- Depth First Search(DFS)
- Breadth First Search(BFS)
- ?

## Dependencies

To install, run: ```pip install -r requirements.txt``` will be installed, pytest, unittest and coverage.


## How to run

The test will run locally

### How to run a single Unit Test

To run the unit test ```pytest test/test_core.py```

### How to run coverage

To run the coverage ```coverage run -m pytest test/test_core.py``` this will generate a .coverage file, then run ```coverage report```

### How each method works

To know how each method is working use the ```__doc__``` command to know the documentation of each method. An example of using ```print(graph.add_edg .__ doc__)```, so documentation of that method can be read via command line.

## How contribuit

## Licence 
    GPL

