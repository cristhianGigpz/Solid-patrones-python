from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def actualizar(self, video):
        pass


class Suscriptor(Observer):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, video):
        print(f"{self.nombre}: a recibido notificación sobre el video: {video}")


class Canal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.suscriptores = []

    def suscribir(self, observer):
        self.suscriptores.append(observer)

    def desuscribir(self, observer):
        self.suscriptores.remove(observer)

    def publicar(self, video):
        for suscriptor in self.suscriptores:
            suscriptor.actualizar(video)


canal = Canal("Mi Canal de YouTube")

suscriptor1 = Suscriptor("Alice")
suscriptor2 = Suscriptor("Bob")
suscriptor3 = Suscriptor("Charlie")

canal.suscribir(suscriptor1)
canal.suscribir(suscriptor2)
canal.suscribir(suscriptor3)

canal.publicar("Cómo aprender Python desde cero")

canal.desuscribir(suscriptor1)

canal.publicar("Curso de Go")
