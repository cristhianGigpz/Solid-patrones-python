from typing import ClassVar


class Soldado:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.tipo = tipo


class TipoSoldado:
    def __init__(self, grupo, uniforme, arma):
        self.grupo = grupo
        self.uniforme = uniforme
        self.arma = arma


class TipoSoldadoFactory:
    _tipos: ClassVar[dict[tuple[str, str, str], TipoSoldado]] = {}

    @classmethod
    def obtener(cls, grupo, uniforme, arma):
        clave = (grupo, uniforme, arma)

        if clave not in cls._tipos:
            cls._tipos[clave] = TipoSoldado(grupo, uniforme, arma)

        return cls._tipos[clave]


tipo1 = TipoSoldadoFactory.obtener("Infantería", "uniforme.png", "rifle")

tipo2 = TipoSoldadoFactory.obtener("Infantería", "uniforme.png", "rifle")

print(tipo1 is tipo2)

soldado = Soldado(20, 100, tipo1)
soldado2 = Soldado(20, 500, tipo1)
