import igraph as ig

from src.utils.graph import (
  create_graph,
  check_is_graph_full,
  check_is_graph_empty
)

from src.utils.vertices import (
  name_vertices,
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
  weighting_edge,
  check_edge_adjacency,
  check_edge_existence,
  get_total_edges
)
