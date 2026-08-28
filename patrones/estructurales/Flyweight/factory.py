from typing import ClassVar


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


class TipoArbolFactory:
    _tipos: ClassVar[dict[tuple[str, str, str], TipoArbol]] = {}

    @classmethod
    def obtener_tipo(cls, nombre, color, textura):
        clave = (nombre, color, textura)

        if clave not in cls._tipos:
            cls._tipos[clave] = TipoArbol(nombre, color, textura)

        return cls._tipos[clave]


pino1 = TipoArbolFactory.obtener_tipo("Pino", "Verde", "pino.png")

pino2 = TipoArbolFactory.obtener_tipo("Pino", "Verde", "pino.png")

print(pino1 is pino2)

pino = TipoArbolFactory.obtener_tipo("Pino", "Verde", "pino.png")

roble = TipoArbolFactory.obtener_tipo("Roble", "Verde oscuro", "roble.png")

bosque = [
    Arbol(10, 20, pino),
    Arbol(30, 50, pino),
    Arbol(80, 20, roble),
    Arbol(100, 70, pino),
]


for planta in bosque:
    print(planta.tipo.nombre)
