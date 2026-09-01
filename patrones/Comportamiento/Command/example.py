from abc import ABC, abstractmethod


class Luz:
    def encender(self):
        print("Luz encendida")

    def apagar(self):
        print("Luz apagada")


class TV:
    def encender(self):
        print("TV encendida")


################################################
class Comando(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

    @abstractmethod
    def deshacer(self):
        pass


class EncenderLuz(Comando):
    def __init__(self, luz):
        self.luz = luz

    def ejecutar(self):
        self.luz.encender()

    def deshacer(self):
        self.luz.apagar()


class ApagarLuz(Comando):
    def __init__(self, luz):
        self.luz = luz

    def ejecutar(self):
        self.luz.apagar()

    def deshacer(self):
        self.luz.encender()


class EncenderTV(Comando):
    def __init__(self, tv):
        self.tv = tv

    def ejecutar(self):
        self.tv.encender()

    def deshacer(self):
        self.tv.apagar()


#############################################


class ControlRemoto:
    def __init__(self):
        self.historial = []

    def ejecutar(self, comando):
        comando.ejecutar()
        self.historial.append(comando)

    def deshacer(self, comando):
        comando.deshacer()


luz = Luz()
tv = TV()

encender = EncenderLuz(luz)
apagar = ApagarLuz(luz)

# comando = EncenderTV(tv)

control = ControlRemoto()

control.ejecutar(encender)
control.ejecutar(apagar)

print(control.historial)

control.deshacer(encender)
# control.ejecutar(comando)


# def guardar():
#     print("Guardando...")


# def ejecutar(comando):
#     comando()


# ejecutar(guardar)
