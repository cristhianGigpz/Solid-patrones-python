from abc import ABC, abstractmethod


class Volador(ABC):
    @abstractmethod
    def volar(self):
        pass


class Aguila(Volador):
    def volar(self):
        print("El águila está volando")


#############################################################


class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass


class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass


class Dormidor(ABC):
    @abstractmethod
    def dormir(self):
        pass


class Empleado(Trabajador, Comedor, Dormidor):
    def trabajar(self):
        print("Empleado trabajando")

    def comer(self):
        print("Empleado comiendo")

    def dormir(self):
        print("Empleado durmiendo")


class Robot(Trabajador):
    def trabajar(self):
        print("Robot trabajando")
