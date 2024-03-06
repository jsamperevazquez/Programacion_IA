from blackjack.baraja import Mano, nuevaBaraja


class Xogo:
    def __init__(self):
        self._xogadores = []
        self._baraja = []

    def xogar(self):
        self._baraja = nuevaBaraja()
        self._baraja.barallar()
        for xogador in self._xogadores:
            xogador.coller_carta(self._baraja.coger())
            xogador.coller_carta(self._baraja.coger())

        while any((xogador.podePedir() for xogador in self._xogadores)):
            for xogador in self._xogadores:
                if xogador.podePedir():
                    print(f"Xogador {xogador.nome}")
                    decision = xogador.decidir(self._xogadores)
                    xogador.actuar(decision, self._baraja)
        ganhador = self.ganhador()
        if ganhador:
            print(f"Temos {len(ganhador)} ganhador")
            print(list((xogador.nome for xogador in ganhador)))
        else:
            print("Non hai gañador")

    def ganhador(self):
        superviventes = [xogador for xogador in self._xogadores if xogador.podeGanhar()]
        if superviventes:
            puntosMax = max((xogador.puntos for xogador in superviventes))
            ganhadores = [xogador for xogador in self._xogadores if xogador.puntos == puntosMax]
            return ganhadores
        else:
            return []

    def addXogador(self, xogador):
        self._xogadores.append(xogador)


class Xogador:
    def __init__(self, nome):
        self._nome = nome
        self._mano = Mano()
        self._estado = EstadoXogadorEnXogo()
        self.estratexia = EstratexiaXogoHumano()

    def podePedir(self):
        return self._estado.podePedir()

    def podeGanhar(self):
        return self._estado.podeGanhar()

    @property
    def nome(self):
        return self._nome

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, valor):
        self._estado = valor

    def decidir(self, xogadores):
        return self.estratexia.decidir(self._mano, xogadores)

    def actuar(self, decision, baralla):
        self._estado.actuar(self, decision, baralla)

    def coller_carta(self, carta):
        self._mano.addCarta(carta)

    @property
    def puntos(self):
        return self._mano.puntos


class EstadoXogador:
    def __init__(self):
        pass

    def decision(self):
        pass

    def actuar(self, xogador, decision, baralla):
        pass


class EstadoXogadorPlantado(EstadoXogador):
    def podePedir(self):
        return False

    def podeGanhar(self):
        return True

    def actuar(self, xogador, decision, baralla):
        raise AccionNonPermitida(decision, xogador)


class EstadoXogadorEnXogo(EstadoXogador):
    def podePedir(self):
        return True

    def podeGanhar(self):
        return True

    def actuar(self, xogador, decision, baralla):
        if decision == 'plantarse':
            xogador._estado = EstadoXogadorPlantado()
        else:
            carta = baralla.coger()
            xogador.coller_carta(carta)
            if xogador.puntos > 21:
                xogador._estado = EstadoXogadorEliminado()


class EstadoXogadorEliminado(EstadoXogador):
    def podePedir(self):
        return False

    def podeGanhar(self):
        return False

    def actuar(self, xogador, decision, baralla):
        raise AccionNonPermitida(decision, xogador)


class EstratexiaXogo():

    def __init__(self):
        pass

    def decidir(self, mano, xogadores):
        pass


class EstratexiaXogoHumano(EstratexiaXogo):

    def decidir(self, mano, xogadores):
        print(f"Cartas: {mano._cartas}")
        print(f"Agora tes {mano.puntos}")
        while True:
            print("Queres outra carta (s/n)")
            d = input()
            if d == 's':
                return 'pedir'
            elif d == 'n':
                return 'plantarse'


class EstratexiaXogoMaquina(EstratexiaXogo):

    def decidir(self, mano, xogadores):
        print(f"Agora tes {mano.puntos}")
        if mano.puntos <= 15 and max(xogador.puntos for xogador in xogadores) >= mano.puntos:
            print(mano.puntos)
            return 'pedir'
        else:
            return 'plantarse'


class AccionNonPermitida(Exception):

    def __init__(self, accion, xogador):
        super().__init__(f"Non se pode {accion} cando o xogador se encontra neste estado")
