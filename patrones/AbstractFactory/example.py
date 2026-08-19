from abc import ABC, abstractmethod


##PRODUCTOS ABSTRACTOS
class Boton(ABC):
    @abstractmethod
    def renderizar(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def renderizar(self):
        pass


## FAMILIA PARA WINDOWS
class BotonWindows(Boton):
    def renderizar(self):
        print("Botón de Windows")


class CheckboxWindows(Checkbox):
    def renderizar(self):
        print("Checkbox de Windows")


### FAMILIA PARA MAC
class BotonMac(Boton):
    def renderizar(self):
        print("Botón de macOS")


class CheckboxMac(Checkbox):
    def renderizar(self):
        print("Checkbox de macOS")


### FAMILIA PARA LINUX
class BotonLinux(Boton):
    def renderizar(self):
        print("Botón de Linux")


class CheckboxLinux(Checkbox):
    def renderizar(self):
        print("Checkbox de Linux")


## FACTORY ABSTRACTA
class UIFactory(ABC):
    @abstractmethod
    def crear_boton(self):
        pass

    @abstractmethod
    def crear_checkbox(self):
        pass


### FACTORY CONCRETA WINDOWS
class WindowsFactory(UIFactory):
    def crear_boton(self):
        return BotonWindows()

    def crear_checkbox(self):
        return CheckboxWindows()


### FACTORY CONCRETA MAC
class MacFactory(UIFactory):
    def crear_boton(self):
        return BotonMac()

    def crear_checkbox(self):
        return CheckboxMac()


class LinuxFactory(UIFactory):
    def crear_boton(self):
        return BotonLinux()

    def crear_checkbox(self):
        return CheckboxLinux()


##APP
class Aplicacion:
    def __init__(self, factory):
        self.boton = factory.crear_boton()
        self.checkbox = factory.crear_checkbox()

    def renderizar(self):
        self.boton.renderizar()
        self.checkbox.renderizar()


##WINDOWS
factory = WindowsFactory()

app = Aplicacion(factory)

app.renderizar()

###MAC

factory2 = MacFactory()

app = Aplicacion(factory2)

app.renderizar()

###LINUX
app = Aplicacion(LinuxFactory())

app.renderizar()
