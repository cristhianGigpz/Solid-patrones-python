from abc import ABC, abstractmethod
from typing import Protocol


class Imprimible(Protocol):
    def imprimir(self) -> None: ...


class Documento:
    def imprimir(self) -> None:
        print("Imprimiendo documento")


def procesar(objeto: Imprimible) -> None:
    objeto.imprimir()


procesar(Documento())


class Ave: ...


class Volador(ABC):
    @abstractmethod
    def volar(self):
        pass


class Aguila(Ave, Volador):
    def volar(self):
        print("Volando")


class Pinguino(Ave):
    def nadar(self):
        print("Nadando")


class Carrito(ABC):
    @abstractmethod
    def agregar(self, producto):
        pass

    @abstractmethod
    def eliminar(self, producto):
        pass

    @abstractmethod
    def obtener_total(self):
        pass


"""
raise NotImplementedError()

o:

pass

o:

return None
"""
