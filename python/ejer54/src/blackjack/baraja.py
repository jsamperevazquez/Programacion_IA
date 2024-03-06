
import itertools
import random


class Carta:

    def __init__(self, palo, numero):
        self._palo = palo
        self._numero = numero

    @property
    def palo(self):
        return self._palo

    @palo.setter
    def palo(self, valor):
        self._palo = valor

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        self._numero = valor

    @property
    def puntos(self):
        if isinstance(self._numero, int):
            return self._numero
        else:
            if self._numero == 'A':
                return [11, 1]
            else:
                return 10

    def __repr__(self):
        return f"<{self._palo},{self._numero}>"


class Mano:

    def __init__(self):
        self._cartas = []

    def addCarta(self, carta: Carta):
        self._cartas.append(carta)

    @property
    def puntos(self):
        p = [carta.puntos for carta in self._cartas]
        simples = [puntos for puntos in p if isinstance(puntos, int)]
        multiples = [puntos for puntos in p if isinstance(puntos, list)]
        if multiples:
            if not simples:
                if len(multiples) == 1:
                    total = [[puntos] for sublist in multiples for puntos in sublist]
                else:
                    unAs = multiples.pop()
                    todasMezclas = list(itertools.product(unAs, *multiples))
                    total = [lista for lista in todasMezclas if sum(lista) < 22]
            else:
                suma = sum(simples)
                todasMezclas = list(itertools.product([suma], *multiples)) if simples else multiples
                todasSumas = [(lista,sum(lista)) for lista in todasMezclas]
                total = [lista for lista,suma in todasSumas if suma < 22]
                if not total:
                    total = [min(todasMezclas, key = lambda t: t[1])]
            return max([sum(lista) for lista in total])
        else:
            return sum(simples)


class Baraja:
    def __init__(self):
        self._cartas = []

    def addCarta(self, carta: Carta):
        self._cartas.append(carta)

    def coger(self):
        return self._cartas.pop()

    def barallar(self):
        random.shuffle(self._cartas)


def nuevaBaraja():
    palos = ['Diamantes', 'Picas', 'Corazones', 'Trevol']
    valores = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J']
    resultado = Baraja()
    for palo in palos:
        for valor in valores:
            resultado.addCarta(Carta(palo, valor))
    return resultado
