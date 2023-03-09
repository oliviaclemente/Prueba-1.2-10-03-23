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
