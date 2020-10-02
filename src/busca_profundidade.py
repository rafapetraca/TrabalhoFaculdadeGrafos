import src.utils as utils

def buscar_em_profundidade(grafo: list, vertice: int, visitados: list) -> bool:
    # Funcao para realizar a busca em profundidade percorrendo os vertices
    if vertice in visitados:
        return False
    visitados.append(vertice)
    for vizinho in utils.selecionar_vertices_adjacentes(grafo, vertice):
        if vizinho not in visitados:
            buscar_em_profundidade(grafo, vizinho, visitados)
