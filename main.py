import src.busca_largura as bl
import src.busca_profundidade as bp

escolha = input('1 - Busca em Largura\n2 - Busca em Profundidade\n')
grafo = [
    [0, 1, 2],
    [1, 0, 3, 4],
    [2, 0, 5, 6],
    [3, 1],
    [4, 1],
    [5, 2],
    [6, 2]
]

if int(escolha) == 1:
    vertice = input(
        "Informe o vertice inicial (entre {} e {}): ".format(
            grafo[0][0], grafo[-1][0])
    )
    vertices_visitados = bl.buscar_em_largura(grafo, int(vertice))
    print('visitados =>', vertices_visitados)

elif int(escolha) == 2:
    visitados = []
    vertice = input(
        "Informe o vertice inicial (entre {} e {}): ".format(
            grafo[0][0], grafo[-1][0])
    )
    bp.buscar_em_profundidade(grafo, int(vertice), visitados)
    print('visitados => ', visitados)

else:
    print('Opção Invalida!')
