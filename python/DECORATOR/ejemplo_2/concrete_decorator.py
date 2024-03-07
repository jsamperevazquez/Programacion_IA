from decorator import Decorator


class Martillo(Decorator):
    def ataque(self):
        return self._decorado.ataque() + 1


class Escudo(Decorator):
    def __init__(self, decorado, defensa=1):
        super().__init__(decorado)
        self._defensa = defensa

    def defensa(self):
        return self._decorado.defensa() + self._defensa


class AnilloDeLaIra(Decorator):
    def ataque(self):
        return self._decorado.ataque() + 1

    def defensa(self):
        return self._decorado.defensa() + 1
