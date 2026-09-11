from abc import ABC, abstractmethod


class Expresion(ABC):
    @abstractmethod
    def interpretar(self, contexto):
        pass


class Palabra(Expresion):
    def __init__(self, palabra):
        self.palabra = palabra

    def interpretar(self, contexto):
        return self.palabra in contexto


class And(Expresion):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

    def interpretar(self, contexto):
        return self.izquierda.interpretar(contexto) and self.derecha.interpretar(
            contexto
        )


class Or(Expresion):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha

    def interpretar(self, contexto):
        return self.izquierda.interpretar(contexto) or self.derecha.interpretar(
            contexto
        )


regla = Palabra("Python")
print(regla.interpretar("Estoy aprendiendo Python"))

regla2 = And(Palabra("Python"), Palabra("Go"))
texto = "Estoy aprendiendo Python y Go"

print(regla2.interpretar(texto))

regla3 = Or(Palabra("Python"), Palabra("Java"))
print(regla3.interpretar("Estoy aprendiendo Python"))

regla4 = And(Palabra("Python"), Or(Palabra("Go"), Palabra("Java")))
print(regla4.interpretar("Estoy aprendiendo Python"))
"""
Python AND (Go OR Java)
Podemos visualizarlo como un árbol:

            AND
           /   \
      Python    OR
               / \
              Go Java
"""
texto = "Uso Python y Go"

print(regla4.interpretar(texto))
