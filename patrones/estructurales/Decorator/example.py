from abc import ABC, abstractmethod


class Bebida(ABC):
    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def precio(self):
        pass


class Cafe(Bebida):
    def descripcion(self):
        return "Café"

    def precio(self):
        return 5


class BebidaDecorator(Bebida):
    def __init__(self, bebida):
        self.bebida = bebida


class Leche(BebidaDecorator):
    def descripcion(self):
        return self.bebida.descripcion() + " + leche"

    def precio(self):
        return self.bebida.precio() + 2


class Chocolate(BebidaDecorator):
    def descripcion(self):
        return self.bebida.descripcion() + " + chocolate"

    def precio(self):
        return self.bebida.precio() + 3


class Crema(BebidaDecorator):
    def descripcion(self):
        return self.bebida.descripcion() + " + crema"

    def precio(self):
        return self.bebida.precio() + 1


# cafe = Cafe()
# bebida = Leche(cafe)
# bebidaConChocolate = Chocolate(bebida)
# bebidaConCrema = Crema(bebida)
bebida = Crema(Chocolate(Leche(Cafe())))

print(bebida.descripcion())
print(bebida.precio())

# @mi_decorador
# def saludar():
#     print("Hola")
