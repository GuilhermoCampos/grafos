def name_vertices(names, graph):
  graph.vs["name"] = names

  return graph

def weight_vertices(weights, graph):
  graph.vs["weight"] = weights

  return graph

def get_vertice_edges(vertice):
  edges = vertice.all_edges()

  names = []

  for edge in edges:
    names.append(edge["name"])

  return names

def get_vertice_attributes(vertice):
  return vertice.attribute_names()

def get_vertice_degree(vertice):
  return vertice.degree()

def check_vertice_adjacency(vertice, searchVertice, graph):
  neighbors = graph.neighbors(vertice)

  for neighbor in neighbors:

    if graph.vs.find(neighbor)["name"] == searchVertice["name"]:
      return True
    else:
      return False

def check_vertice_existence(vertice, graph):
  for v in graph.vs:
    if v["name"] == vertice:
      return True

  return False

def get_total_vertices(graph):
  return graph.vcount()

