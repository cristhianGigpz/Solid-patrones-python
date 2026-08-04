class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def calcular_impuesto(self): ...

    def aplicar_descuento(self): ...

    def exportar_pdf(self): ...

    def guardar_bd(self): ...

    def enviar_email(self): ...


class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b


# class Pedido:
#     def __init__(self, repositorio):
#         self.repositorio = repositorio

#     def guardar(self):
#         self.repositorio.insertar(self)


class Pedido:
    def calcular_total(self):
        print("Calculando total")

    def guardar_bd(self):
        print("Guardando en la base de datos")

    def enviar_email(self):
        print("Enviando correo")

    def generar_pdf(self):
        print("Generando PDF")


def main():
    print("Principios SOLID y Patrones de Diseño con Python")


if __name__ == "__main__":
    main()

"""
¿Qué son los principios SOLID?

SOLID es un conjunto de cinco principios propuestos por Robert C. Martin 
(Uncle Bob) para crear software más mantenible, flexible y escalable.

Cada letra representa un principio:

Letra	Principio	Objetivo
S	Single Responsibility Principle - Una clase debe tener una única responsabilidad.
O	Open/Closed Principle - El código debe poder extenderse sin modificar lo existente.
L	Liskov Substitution Principle - Las clases hijas deben poder sustituir correctamente 
	a la clase padre.
I	Interface Segregation Principle	- Es mejor tener varias interfaces pequeñas que una muy 
	grande.
D	Dependency Inversion Principle - Depender de abstracciones y no de implementaciones 
	concretas.

"""
