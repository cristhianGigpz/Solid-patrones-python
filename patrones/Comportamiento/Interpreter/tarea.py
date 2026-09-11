"""
mediante un árbol:--------------------

             OR
            /  \
          AND  Premium
         /   \
      Admin  Activo
"""

from abc import ABC, abstractmethod


class Expresion(ABC):
    @abstractmethod
    def interpretar(self, contexto):
        pass


class Admin(Expresion):
    def interpretar(self, contexto):
        return "Admin" in contexto


class Activo(Expresion):
    def interpretar(self, contexto):
        return "Activo" in contexto


class Premium(Expresion):
    def interpretar(self, contexto):
        return "Premium" in contexto


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


usuario = {"Admin": True, "Activo": True, "Premium": False}

regla = And(Admin(), Activo())
print(regla.interpretar(usuario))

regla2 = Or(And(Admin(), Activo()), Premium())
print(regla2.interpretar(usuario))
