def name_vertices(names, graph):
  graph.vs["name"] = names

  return graph

def get_vertice_edges(vertice):
  return vertice.all_edges()

def get_vertice_attributes(vertice):
  return vertice.attribute_names()

def get_vertice_degree(vertice):
  return vertice.degree()

def check_vertice_adjacency(vertice, searchVertice, graph):
  neighbors = graph.neighbors(vertice)

  for neighbor in neighbors:
    if neighbor == searchVertice:
      return True
    else :
      return False

def check_vertice_existence(vertice, graph):
  return vertice in graph.vs

def get_total_vertices(graph):
  return graph.vcount()

