import igraph as ig

def create_edge(edges, graph):
  graph.add_edges(edges)


def remove_edge(edge, graph):
  edge_id = graph.get_eid(edge[0], edge[1])
  graph.delete_edges(edge_id)


def weighting_edge(weights, graph):
  graph.es['weight'] = weights


def name_edges(edges, graph):
  graph.es['name'] = edges


def check_edge_adjacency(graph):
  return graph.get_adjacency()


def check_edge_existence(edge, graph):
  for e in graph.es:
    if e["name"] == edge:
      return True

  return False


def get_total_edges(graph):
  return graph.ecount()
