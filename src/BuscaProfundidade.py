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


def selecionar_vertices_adjacentes(grafo, vertice):
    # Funcao para adicionar os vertices que estao por vir (pilha)
    adj = []
    for i in range(1, len(grafo[vertice])):
        adj.append(grafo[vertice][i])
    return adj


def buscar_em_profundidade(grafo, vertice, visitados):
    # Funcao para realizar a busca em profundidade percorrendo os vertices
    if vertice in visitados:
        return False
    visitados.append(vertice)
    for vizinho in selecionar_vertices_adjacentes(grafo, vertice):
        if vizinho not in visitados:
            buscar_em_profundidade(grafo, vizinho, visitados)


# Pedir o vertice para inciar a busca
visitados = []
vertice = input("Informe o vertice inicial: ")
buscar_em_profundidade(grafo, int(vertice), visitados)

print('visitados => ', visitados)
