from abc import ABC, abstractmethod


class RepositorioUsuario(ABC):
    @abstractmethod
    def buscar(self, id):
        pass

    @abstractmethod
    def guardar(self, usuario):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass


class Legible(ABC):
    @abstractmethod
    def leer(self):
        pass


class Escribible(ABC):
    @abstractmethod
    def escribir(self, contenido):
        pass


class Eliminable(ABC):
    @abstractmethod
    def eliminar(self):
        pass


class ArchivoSoloLectura(Legible):
    def leer(self):
        return "Contenido"


class ArchivoNormal(Legible, Escribible, Eliminable):
    def leer(self):
        return "Contenido"

    def escribir(self, contenido):
        print(f"Guardando: {contenido}")

    def eliminar(self):
        print("Archivo eliminado")
