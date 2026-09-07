from abc import ABC, abstractmethod


class EstadoSemaforo(ABC):
    @abstractmethod
    def cambiar(self, semaforo):
        pass


class Rojo(EstadoSemaforo):
    def cambiar(self, semaforo):
        print("Cambiando a verde")
        semaforo.estado = Verde()


class Verde(EstadoSemaforo):
    def cambiar(self, semaforo):
        print("Cambiando a amarillo")
        semaforo.estado = Amarillo()


class Amarillo(EstadoSemaforo):
    def cambiar(self, semaforo):
        print("Cambiando a rojo")
        semaforo.estado = Rojo()


class Semaforo:
    def __init__(self):
        self.estado = Rojo()

    def cambiar(self):
        self.estado.cambiar(self)


semaforo = Semaforo()

semaforo.cambiar()
semaforo.cambiar()
semaforo.cambiar()
