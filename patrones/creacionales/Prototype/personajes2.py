import copy


class Personaje:
    def __init__(self, nombre, habilidades):
        self.nombre = nombre
        self.habilidades = habilidades

    def clonar(self):
        return copy.deepcopy(self)


mago = Personaje("Mago", ["fuego", "hielo"])

mago2 = mago.clonar()


mago2.habilidades.append("teletransporte")

print(mago.habilidades)
print(mago2.habilidades)
