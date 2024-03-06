
from blackjack.xogo import Xogador, AccionNonPermitida
from blackjack.baraja import Carta, Baraja
import pytest


def test_estado_xogador():
    xogador = Xogador("Xogador1")
    baraja = Baraja()
    baraja.addCarta(Carta('Diamantes', 10))
    baraja.addCarta(Carta('Diamantes', 5))
    baraja.addCarta(Carta('Picas', 10))
    xogador.actuar('pedir', baraja)
    xogador.actuar('pedir', baraja)
    assert xogador.puntos == 15
    assert xogador.podePedir() is True
    assert xogador.podeGanhar() is True
    xogador.actuar('pedir', baraja)
    assert xogador.puntos == 25
    assert xogador.podePedir() is False
    assert xogador.podeGanhar() is False


def test_estado_xogador_plantado():
    xogador = Xogador("Xogador1")
    baraja = Baraja()
    baraja.addCarta(Carta('Diamantes', 10))
    baraja.addCarta(Carta('Diamantes', 5))
    baraja.addCarta(Carta('Picas', 10))
    xogador.actuar('pedir', baraja)
    xogador.actuar('pedir', baraja)
    assert xogador.puntos == 15
    assert xogador.podePedir() is True
    assert xogador.podeGanhar() is True
    xogador.actuar('plantarse', baraja)
    assert xogador.puntos == 15
    assert xogador.podePedir() is False
    assert xogador.podeGanhar() is True


def test_estado_xogador_eliminador():
    xogador = Xogador("Xogador1")
    baraja = Baraja()
    baraja.addCarta(Carta('Diamantes', 10))
    baraja.addCarta(Carta('Diamantes', 5))
    baraja.addCarta(Carta('Picas', 10))
    xogador.actuar('pedir', baraja)
    xogador.actuar('pedir', baraja)
    assert xogador.puntos == 15
    assert xogador.podePedir() is True
    assert xogador.podeGanhar() is True
    xogador.actuar('pedir', baraja)
    assert xogador.puntos == 25
    with pytest.raises(AccionNonPermitida):
        xogador.actuar('pedir', baraja)
