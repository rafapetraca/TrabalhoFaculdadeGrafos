#minimum spanning tree (MST)
from collections import defaultdict

# Classe para representar o grafico


class Graph:

	def __init__(self, vertices):
		self.V = vertices # No. de vertices
		self.graph = [] #Armazenar o grafo
		

	# Add vizinhos
	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])

	# Funcao que faz a uniao de x e y
	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)

		#Pega a menor parte da arvore
		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot

		# Caso a parte for igual
		else:
			parent[yroot] = xroot
			rank[xroot] += 1

	# Funcao principal para construir a arvore
	def KruskalMST(self):

		result = [] #Onde vamos guardar os resultados
		#Para sortear os vizinhos
		i = 0
		
		# Variavel para os resultas[]
		e = 0

#Passo 1: Classifique todos em ordem crescente
		self.graph = sorted(self.graph, 
							key=lambda item: item[2])

		parent = []
		rank = []

	
		for node in range(self.V):
			parent.append(node)
			rank.append(0)

	
		while e < self.V - 1:

			# Pegue o menor vizinho e incremente
			u, v, w = self.graph[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent, v)

			if x != y:
				e = e + 1
				result.append([u, v, w])
				self.union(parent, rank, x, y)


		minimumCost = 0
		print ("Edges in the constructed MST")
		for u, v, weight in result:
			minimumCost += weight
			print("%d -- %d == %d" % (u, v, weight))
		print("Minimum Spanning Tree" , minimumCost)

g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

# Chamada da função
g.KruskalMST()

