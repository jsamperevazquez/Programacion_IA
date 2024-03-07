from abc import ABC, abstractmethod


class Xogador(ABC):
    @abstractmethod
    def ataque(self):
        pass

    @abstractmethod
    def defensa(self):
        pass

    @abstractmethod
    def multiplicador(self, valor):
        pass
