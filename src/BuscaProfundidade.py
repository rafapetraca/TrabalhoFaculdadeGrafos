import utils

# Estrutura do grafo ja pronta
grafo = [
    [0, 1, 2],
    [1, 0, 3, 4],
    [2, 0, 5, 6],
    [3, 1],
    [4, 1],
    [5, 2],
    [6, 2]
]


def buscar_em_profundidade(grafo: list, vertice: int, visitados: list) -> bool:
    # Funcao para realizar a busca em profundidade percorrendo os vertices
    if vertice in visitados:
        return False
    visitados.append(vertice)
    for vizinho in utils.selecionar_vertices_adjacentes(grafo, vertice):
        if vizinho not in visitados:
            buscar_em_profundidade(grafo, vizinho, visitados)


# Pedir o vertice para inciar a busca
visitados = []
vertice = input(
    "Informe o vertice inicial (entre {} e {}): ".format(
        grafo[0][0], grafo[-1][0])
)
buscar_em_profundidade(grafo, int(vertice), visitados)

print('visitados => ', visitados)
