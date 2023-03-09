class Polinomio:
    def __init__(self):
        self.terminos = []

    def agregar_termino(self, coeficiente, exponente):
        self.terminos.append((coeficiente, exponente))

    def eliminar_termino(self, exponente):
        for i, term in enumerate(self.terminos):
            if term[1] == exponente:
                del self.terminos[i]
                return

    def existe_termino(self, exponente):
        for term in self.terminos:
            if term[1] == exponente:
                return True
        return False

    def obtener_valor(self, x):
        valor = 0
        for term in self.terminos:
            valor += term[0] * x ** term[1]
        return valor

import unittest

class TestPolinomio(unittest.TestCase):
    def setUp(self):
        self.p = Polinomio()
        self.p.agregar_termino(2, 3)
        self.p.agregar_termino(1, 2)
        self.p.agregar_termino(3, 0)

    def test_eliminar_termino(self):
        self.p.eliminar_termino(2)
        self.assertEqual(len(self.p.terminos), 2)
        self.assertFalse(self.p.existe_termino(2))

    def test_existe_termino(self):
        self.assertTrue(self.p.existe_termino(2))
        self.assertFalse(self.p.existe_termino(1))

    def test_obtener_valor(self):
        self.assertEqual(self.p.obtener_valor(2), 28)
        self.assertEqual(self.p.obtener_valor(0), 3)

if __name__ == '__main__':
    unittest.main()
