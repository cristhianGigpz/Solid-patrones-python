import copy


class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.armas = ["pistola", "rifle"]

    def clonar(self):
        return copy.deepcopy(self)


soldado = Personaje("Soldado", 100, 20)

soldado2 = soldado.clonar()
soldado3 = soldado.clonar()

soldado2.nombre = "Soldado élite"
soldado2.ataque = 40

print(soldado is soldado2)

print(soldado.nombre)
print(soldado2.nombre)

original = Personaje("Soldado", 100, 20)

copia = original.clonar()

print(original is copia)
copia.armas.append("arco")
print(original.armas is copia.armas)
