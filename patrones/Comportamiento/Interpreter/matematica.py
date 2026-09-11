from abc import ABC, abstractmethod


class Expresion(ABC):
    @abstractmethod
    def interpretar(self, contexto):
        pass


class Numero(Expresion):
    def __init__(self, valor):
        self.valor = valor

    def interpretar(self, contexto=None):
        return self.valor


class Suma(Expresion):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

    def interpretar(self, contexto=None):
        return self.izquierda.interpretar() + self.derecha.interpretar()


operacion = Suma(Numero(10), Numero(5))

print(operacion.interpretar())

##10 + (5 + 3)
operacion = Suma(Numero(10), Suma(Numero(5), Numero(3)))
print(operacion.interpretar())
