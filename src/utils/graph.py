import igraph as ig
from src.utils.edges import (
  check_edge_adjacency,
)

def create_graph(tamanho, edges):
  return ig.Graph(n=tamanho, edges=edges)

def check_is_graph_full(graph):
  vertices = graph.vs

  for vertex in vertices:
    if vertex.degree() != graph.vcount() - 1:
      return False
    else: return True

  return

def check_is_graph_empty(graph):
  if(graph.es == 0): return True
  else: return False

def get_graph_edges(graph):
  edges = graph.es()

  names = []

  for edge in edges:
    names.append(edge["name"])

  return names

def get_graph_adjacency_matrix(graph):
  return graph.get_adjacency()

def get_graph_adjacency_list(graph):
  return graph.get_adjlist()