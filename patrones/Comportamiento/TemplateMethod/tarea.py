from abc import ABC, abstractmethod


class Bebida(ABC):
    def preparar(self):
        self.hervir_agua()
        self.preparar_ingrediente()
        self.servir()
        self.agregar_complemento()

    def hervir_agua(self):
        print("Hirviendo agua")

    @abstractmethod
    def preparar_ingrediente(self):
        pass

    def servir(self):
        print("Sirviendo en una taza")

    @abstractmethod
    def agregar_complemento(self):
        pass


class Te(Bebida):
    def preparar_ingrediente(self):
        print("Preparando té")

    def agregar_complemento(self):
        print("Agregando limón")


class Cafe(Bebida):
    def preparar_ingrediente(self):
        print("Preparando café")

    def agregar_complemento(self):
        print("Agregando leche y azúcar")


te = Te()
te.preparar()
print("---------------------")
cafe = Cafe()
cafe.preparar()
