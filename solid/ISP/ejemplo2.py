from abc import ABC, abstractmethod


class Imprimible(ABC):
    @abstractmethod
    def imprimir(self):
        pass


class Escaneable(ABC):
    @abstractmethod
    def escanear(self):
        pass


class Fax(ABC):
    @abstractmethod
    def enviar_fax(self):
        pass


class ImpresoraMultifuncion(Imprimible, Escaneable, Fax):
    def imprimir(self):
        print("Imprimiendo")

    def escanear(self):
        print("Escaneando")

    def enviar_fax(self):
        print("Enviando fax")


class ImpresoraBasica(Imprimible):
    def imprimir(self):
        print("Imprimiendo")


def imprimir_documento(dispositivo: Imprimible):
    dispositivo.imprimir()


imprimir_documento(ImpresoraBasica())

imprimir_documento(ImpresoraMultifuncion())
