import igraph as ig
import app

def create_graph(vertices):
  return ig.Graph(n=vertices)

def check_is_graph_full(graph):
  isFull = False

  for vertice in graph:
    for other_vertice in graph:
      isFull = app.check_edge_adjacency(vertice, other_vertice, graph)

  return isFull

def check_is_graph_empty():
  return