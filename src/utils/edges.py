import igraph as ig

def create_edge(edges, graph):
  graph.add_edges(edges)

def remove_edge(edge, graph):
  edge_id = graph.get_eid(edge[0], edge[1])
  graph.delete_edges(edge_id)

def weighting_edge(weights, graph):
  graph.es['weight'] = weights

def check_edge_adjacency(edge, graph):
  has_adjacency = False

  
  return has_adjacency

def check_edge_existence(edge, graph):
  for e in graph.get_edgelist():
    if e[0] == edge[0] and e[1] == edge[1]:
      return True
  
  return False

def get_total_edges(graph):
  return graph.ecount()
