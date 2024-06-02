from abc import ABC, abstractmethod


class Personaje(ABC):
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 1
        self.sprite = " "  # Estos es para el sprited de cada personaje

    def atacar(self, objetivo):
        pass

    @abstractmethod
    def moverse(self):
        pass

    @abstractmethod
    def detruirse(self, vida):
        pass
