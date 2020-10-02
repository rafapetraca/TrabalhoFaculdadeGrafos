import unittest
import src.utils as utils


class TestUtils(unittest.TestCase):

    def test_encontrar_vizinhos(self):
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
        adjacentes_esperados = [0, 5, 6]
        adjacentes = utils.selecionar_vertices_adjacentes(grafo, vertice)
        self.assertEqual(adjacentes, adjacentes_esperados)


if __name__ == '__main__':
    unittest.main()
