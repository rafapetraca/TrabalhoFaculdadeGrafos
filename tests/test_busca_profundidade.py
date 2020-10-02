import unittest
import src.busca_profundidade as bp


class TestBuscaProfundidade(unittest.TestCase):

    def test_buscar_em_profundidade(self):
        grafo = [
            [0, 1, 2],
            [1, 0, 3, 4],
            [2, 0, 5, 6],
            [3, 1],
            [4, 1],
            [5, 2],
            [6, 2]
        ]
        vertice = 1
        visitados = []
        resultado = bp.buscar_em_profundidade(
            grafo, vertice, visitados)
        self.assertIsNone(resultado, None)


if __name__ == '__main__':
    unittest.main()
