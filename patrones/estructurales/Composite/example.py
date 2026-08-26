from abc import ABC, abstractmethod


class Elemento(ABC):
    @abstractmethod
    def obtener_tamaño(self):
        pass


class Archivo(Elemento):
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño

    def obtener_tamaño(self):
        return self.tamaño


class Carpeta(Elemento):
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def obtener_tamaño(self):
        return sum(elemento.obtener_tamaño() for elemento in self.elementos)


foto = Archivo("foto.jpg", 5)
video = Archivo("video.mp4", 100)

multimedia = Carpeta("Multimedia")

multimedia.agregar(foto)
multimedia.agregar(video)

print(multimedia.obtener_tamaño())

documento = Archivo("reporte.pdf", 20)

documentos = Carpeta("Documentos")
documentos.agregar(documento)

raiz = Carpeta("Inicio")

raiz.agregar(multimedia)
raiz.agregar(documentos)


print(raiz.obtener_tamaño())


def mostrar_tamaño(elemento):
    print(elemento.obtener_tamaño())


mostrar_tamaño(Archivo("foto.jpg", 5))
mostrar_tamaño(documentos)
