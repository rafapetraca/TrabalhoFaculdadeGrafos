import src.utils as utils


def buscar_em_largura(grafo: list, vertice: int) -> list:
    # Funcao para realizar a busca em largura - buscados os vizinhos
    #   -> faz uma lista de vertices ja visitados
    #   -> faz uma lista de vestices "para visitar"
    lista = []
    visitados = []
    visitados.append(vertice)
    lista.append(vertice)

    # Verificacao dos vertices que estao sendo percorridos
    #  -> se eles estiverem na lista de ja visitados
    while len(lista):
        vertice_atual = lista.pop(0)
        for vizinho in \
                utils.selecionar_vertices_adjacentes(grafo, vertice_atual):
            if vizinho not in visitados:
                lista.append(vizinho)
                visitados.append(vizinho)

    return visitados
