class PartidaMemento:
    def __init__(self, nivel, vida):
        self.nivel = nivel
        self.vida = vida


class Personaje:
    def __init__(self):
        self.nivel = 1
        self.vida = 100

    def guardar(self):
        return PartidaMemento(self.nivel, self.vida)

    def restaurar(self, memento):
        self.nivel = memento.nivel
        self.vida = memento.vida


personaje = Personaje()

checkpoint = personaje.guardar()

personaje.nivel = 5
personaje.vida = 50

print(f"Nivel: {personaje.nivel}, Vida: {personaje.vida}")

personaje.restaurar(checkpoint)

print(f"Nivel: {personaje.nivel}, Vida: {personaje.vida}")
