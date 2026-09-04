class PersonajeMemento:
    def __init__(self, nivel, vida, monedas=0):
        self.nivel = nivel
        self.vida = vida
        self.monedas = monedas


class Personaje:
    def __init__(self):
        self.vida = 100
        self.monedas = 0
        self.nivel = 1

    def guardar(self):
        return PersonajeMemento(self.nivel, self.vida, self.monedas)

    def restaurar(self, memento):
        self.nivel = memento.nivel
        self.vida = memento.vida
        self.monedas = memento.monedas


class Historial:
    def __init__(self):
        self.estados = []

    def guardar(self, memento):
        self.estados.append(memento)

    def deshacer(self):
        if self.estados:
            return self.estados.pop()


personaje = Personaje()

checkpoint = personaje.guardar()

personaje.vida = 20
personaje.monedas = 500

print(f"Nivel: {personaje.nivel}, Vida: {personaje.vida}, Monedas: {personaje.monedas}")

personaje.restaurar(checkpoint)
print(f"Nivel: {personaje.nivel}, Vida: {personaje.vida}, Monedas: {personaje.monedas}")
