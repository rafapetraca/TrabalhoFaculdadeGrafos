def selecionar_vertices_adjacentes(grafo: list, vertice: int) -> list:
    # Funcao para adicionar os vertices que estao por vir (pilha)
    adjacentes = []
    for i in range(1, len(grafo[vertice])):
        adjacentes.append(grafo[vertice][i])
    return adjacentes
