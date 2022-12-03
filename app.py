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

graph = create_graph(3, [[0,1], [1,2]])
name_vertices(['Grafo', 'Bem', 'Legal'], graph)
weight_vertices(['2', '3', '4'], graph)
name_edges(["grafo-bem", "bem-legal"], graph)
weighting_edge(['2', '3'], graph)

print('LISTA DE ADJACENCIA')
print(get_graph_adjacency_list(graph))

print('MATRIZ DE ADJACENCIA')
print(get_graph_adjacency_matrix(graph))


create_edge([(2, 0)], graph)
name_edges(["grafo-bem", "bem-legal", "legal-grafo"], graph)

print('REMOVE UMA ARESTA DE UM GRAFO')
remove_edge([0,1], graph)
print("Novo total de arestas")
print(get_total_edges(graph))
print("Arestas")
print(get_graph_edges(graph))

print('ADICIONA UMA ARESTA AO GRAFO')
create_edge([(2, 0)], graph)
name_edges(["grafo-bem", "bem-legal", "legal-grafo"], graph)
print("Novo total de arestas")
print(get_total_edges(graph))
print("Arestas")
print(get_graph_edges(graph))


print("CHECAGEM SE O GRAFO É CHEIO")
print(check_is_graph_empty(graph))


print("CHECAGEM SE O GRAFO É VAZIO")
print(check_is_graph_full(graph))

print('PEGA O TOTAL DE ARESTAS DE UM GRAFO')
print(get_total_edges(graph))

print("PEGA O TOTAL DE VÉRTICES DE UM GRAFO")
print(get_total_vertices(graph))

print("CHECA EXISTENCIA DE UMA ARESTA (NÃO EXISTE)")
print(check_edge_existence('não-existe', graph))
print("CHECA EXISTENCIA DE UMA ARESTA (EXISTE)")
print(check_edge_existence('bem-legal', graph))

print("ADJACENCIA DE ARESTAS")
print(check_edge_adjacency(graph))

print("PEGA TODAS AS ARESTAS DE UM DETERMINADO VÉRTICE")
print(get_vertice_edges(graph.vs.find(name="Legal")))

print('CHECA A EXISTENCIA DE UM VERTICE (EXISTE)')
print(check_vertice_existence("Grafo", graph))
print('CHECA A EXISTENCIA DE UM VERTICE (NÃO EXISTE)')
print(check_vertice_existence("não-existe", graph))

print("CHECAGEM DE ADJACENCIA DE UM VÉRTICE (NÃO EXISTE)")
print(check_vertice_adjacency(graph.vs.find(name="Grafo"), graph.vs.find(name="Legal"), graph))
print("CHECAGEM DE ADJACENCIA E EXISTENCIA DE UM VÉRTICE (EXISTE)")
print(check_vertice_adjacency(graph.vs.find(name="Grafo"), graph.vs.find(name="Bem"), graph))

print('GRAU DO VERTICE `GRAFO`')
print(get_vertice_degree(graph.vs.find(name="Grafo")))
print('GRAU DO VERTICE `BEM`')
print(get_vertice_degree(graph.vs.find(name="Bem")))
print('GRAU DO VERTICE `LEGAL`')
print(get_vertice_degree(graph.vs.find(name="Legal")))

print('NOME E PESO DOS VÉRTICES')
print(graph.vs["name"])
print(graph.vs["weight"])
print('\n')
print('NOME E PESO DAS ARESTAS')
print(graph.es["name"])
print(graph.es["weight"])

print('\n')

print('\n')

print("PEGA TODAS AS ARESTAS DE UM GRAFO")
print(get_graph_edges(graph))