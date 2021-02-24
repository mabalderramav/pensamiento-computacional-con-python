import unittest


def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False


class PruebaDeCristal(unittest.TestCase):
    def test_es_mayor_de_edad(self):
        edad = 20

        resultado = es_mayor_de_edad(edad)
        self.assertTrue(resultado)

    def test_es_menor_edad(self):
        edad = 8

        resultado = es_mayor_de_edad(edad)
        self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main()
