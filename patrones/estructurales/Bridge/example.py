from abc import ABC, abstractmethod


class Dispositivo(ABC):
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass


class TV(Dispositivo):
    def encender(self):
        print("TV encendida")

    def apagar(self):
        print("TV apagada")


class Radio(Dispositivo):
    def encender(self):
        print("Radio encendida")

    def apagar(self):
        print("Radio apagada")


class Proyector(Dispositivo):
    def encender(self):
        print("Proyector encendido")

    def apagar(self):
        print("Proyector apagado")


class Control:
    def __init__(self, dispositivo):
        self.dispositivo = dispositivo

    def encender(self):
        self.dispositivo.encender()

    def apagar(self):
        self.dispositivo.apagar()


class ControlAvanzado(Control):
    def silenciar(self):
        print("Dispositivo silenciado")


control = Control(TV())

control.encender()
control.apagar()

control = Control(Radio())

control.encender()
control.apagar()

control = ControlAvanzado(TV())

control.encender()
control.silenciar()

control = ControlAvanzado(Radio())
control.encender()
control.silenciar()

control = Control(Proyector())
control.encender()
control.apagar()

control = ControlAvanzado(Proyector())
control.silenciar()
