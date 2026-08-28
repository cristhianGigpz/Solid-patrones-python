class Arbol:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.tipo = tipo


class TipoArbol:
    def __init__(self, nombre, color, textura):
        self.nombre = nombre
        self.color = color
        self.textura = textura


# arbol1 = Arbol("Pino", "Verde", "pino.png", 10, 20)
# arbol2 = Arbol("Pino", "Verde", "pino.png", 50, 80)
pino = TipoArbol("Pino", "Verde", "pino.png")

arbol1 = Arbol(10, 20, pino)
arbol2 = Arbol(50, 80, pino)
arbol3 = Arbol(100, 30, pino)

print(arbol1.tipo is arbol2.tipo)
