from abc import ABC, abstractmethod


class Descuento(ABC):
    @abstractmethod
    def calcular(self, precio):
        pass


class SinDescuento(Descuento):
    def calcular(self, precio):
        return precio


class DescuentoVIP(Descuento):
    def calcular(self, precio):
        return precio * 0.80


class Carrito:
    def __init__(self, descuento):
        self.descuento = descuento

    def total(self, precio):
        return self.descuento.calcular(precio)


carrito = Carrito(DescuentoVIP())

print(carrito.total(100))


def descuento_normal(precio):
    return precio


def descuento_vip(precio):
    return precio * 0.80


class Carrito2:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def total(self, precio):
        return self.estrategia(precio)


carrito2 = Carrito2(descuento_vip)

print(carrito2.total(100))
