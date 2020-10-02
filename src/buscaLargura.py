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


def buscar_em_largura(grafo, vertice):
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
        v = lista.pop(0)
        for vizinho in utils.selecionar_vertices_adjacentes(grafo, v):
            if not vizinho in visitados:
                lista.append(vizinho)
                visitados.append(vizinho)

    print('visitados =>', visitados)


# Pedir o vertice para iniciar a busca
vertice = input(
    "Informe o vertice inicial (entre {} e ){}): ".format(
        grafo[0][0], grafo[-1][0])
)
buscar_em_largura(grafo, int(vertice))
