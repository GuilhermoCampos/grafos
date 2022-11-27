from src.utils.graph import (
  create_graph,
  check_is_graph_full,
  check_is_graph_empty,
  get_graph_edges,
  get_graph_adjacency_matrix,
  get_graph_adjacency_list
)

from src.utils.vertices import (
  name_vertices,
  weight_vertices,
  get_vertice_edges,
  get_vertice_attributes,
  get_vertice_degree,
  check_vertice_adjacency,
  check_vertice_existence,
  get_total_vertices
)

from src.utils.edges import (
  create_edge,
  remove_edge,
  name_edges,
  weighting_edge,
  check_edge_adjacency,
  check_edge_existence,
  get_total_edges
)

graph = create_graph(3, [[0,1]])

name_vertices(['André', 'Guilherme', 'Lucas'], graph)
weight_vertices(['2', '3', '4'], graph)
name_edges(["andré-guilherme", "guilherme-lucas", "lucas-andré"], graph)

print('VERTICES TEST')
print('\n')
print(graph.vs["name"])
print(graph.vs["weight"])
print(graph.vs.find(name="André").attributes())
print(get_vertice_attributes(graph.vs.find(name="André")))
print(get_vertice_degree(graph.vs.find(name="André")))
print(check_vertice_adjacency(graph.vs.find(name="André"), graph.vs.find(name="Guilherme"), graph))
print(check_vertice_existence("André", graph))
print(get_vertice_edges(graph.vs.find(name="André")))
print(get_total_vertices(graph))

print('\n')
print("GRAPH TEST")
print(check_is_graph_empty(graph))
print(check_is_graph_full(graph))
print('Lista de Adjacencia')
print(get_graph_adjacency_list(graph))
print('Matriz de Adjacencia')
print(get_graph_adjacency_matrix(graph))

print('\n')
print('EDGES TEST')
print(get_total_edges(graph))
print(get_graph_edges(graph))
print('adding edge')
create_edge([(1, 2)], graph)
print(get_total_edges(graph))
name_edges(["andré-guilherme", "guilherme-lucas"], graph)
print(get_graph_edges(graph))
print('removing edge')
remove_edge([0,1], graph)
print(get_total_edges(graph))
print(get_graph_edges(graph))
weighting_edge(['2'], graph)
print(graph.es["weight"])
print(check_edge_adjacency(graph))
print(check_edge_existence('andré-guilherme', graph))
