from abc import ABC, abstractmethod


class Text(ABC):
    @abstractmethod
    def render(self):
        pass
