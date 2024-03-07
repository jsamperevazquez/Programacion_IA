from component import Xogador


class XogadorIni(Xogador):

    def __init__(self):
        self._vida = 3

    def ataque(self):
        return 5

    def defensa(self):
        return 10

    def multiplicador(self, valor):
        return self._vida * valor

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        self._vida = valor
