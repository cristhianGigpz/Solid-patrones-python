from abc import ABC, abstractmethod


class Elemento(ABC):
    @abstractmethod
    def aceptar(self, visitor):
        pass


class Circulo(Elemento):
    def __init__(self, radio):
        self.radio = radio

    def aceptar(self, visitor):
        return visitor.visitar_circulo(self)


class Cuadrado(Elemento):
    def __init__(self, lado):
        self.lado = lado

    def aceptar(self, visitor):
        return visitor.visitar_cuadrado(self)


class Triangulo(Elemento):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def aceptar(self, visitor):
        return visitor.visitar_triangulo(self)


class Visitor(ABC):
    @abstractmethod
    def visitar_circulo(self, circulo):
        pass

    @abstractmethod
    def visitar_cuadrado(self, cuadrado):
        pass

    @abstractmethod
    def visitar_triangulo(self, triangulo):
        pass


class AreaVisitor(Visitor):
    def visitar_circulo(self, circulo):
        return 3.14159 * (circulo.radio**2)

    def visitar_cuadrado(self, cuadrado):
        return cuadrado.lado**2

    def visitar_triangulo(self, triangulo):
        return 0.5 * triangulo.base * triangulo.altura


class DescripcionVisitor(Visitor):
    def visitar_circulo(self, circulo):
        return f"Circulo con radio {circulo.radio}"

    def visitar_cuadrado(self, cuadrado):
        return f"Cuadrado con lado {cuadrado.lado}"

    def visitar_triangulo(self, triangulo):
        return f"Triangulo con base {triangulo.base} y altura {triangulo.altura}"


circulo = Circulo(5)
cuadrado = Cuadrado(4)
triangulo = Triangulo(3, 6)

area_visitor = AreaVisitor()
descripcion_visitor = DescripcionVisitor()

print(f"Área del círculo: {circulo.aceptar(area_visitor)}")
print(f"Área del cuadrado: {cuadrado.aceptar(area_visitor)}")
print(f"Área del triángulo: {triangulo.aceptar(area_visitor)}")

print(f"Descripción del círculo: {circulo.aceptar(descripcion_visitor)}")
print(f"Descripción del cuadrado: {cuadrado.aceptar(descripcion_visitor)}")
print(f"Descripción del triángulo: {triangulo.aceptar(descripcion_visitor)}")
