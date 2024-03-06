from blackjack.xogo import Xogo, Xogador, EstratexiaXogoMaquina

if __name__ == "__main__":
    xogo = Xogo()
    xogo.addXogador(Xogador("Xogador1"))
    xogo.addXogador(Xogador("Xogador2"))
    maquina = Xogador("Maquina")
    maquina.estratexia = EstratexiaXogoMaquina()
    xogo.addXogador(maquina)
    xogo.xogar()
