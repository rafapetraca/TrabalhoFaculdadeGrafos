import unittest
import src.busca_largura as bl


class TestBuscaLargura(unittest.TestCase):

    def test_buscar_em_largura(self):
        grafo = [
            [0, 1, 2],
            [1, 0, 3, 4],
            [2, 0, 5, 6],
            [3, 1],
            [4, 1],
            [5, 2],
            [6, 2]
        ]
        vertice = 2
        visitados_esperados = [2, 0, 5, 6, 1, 3, 4]
        visitados = bl.buscar_em_largura(grafo, vertice)
        self.assertEqual(visitados, visitados_esperados)


if __name__ == '__main__':
    unittest.main()
