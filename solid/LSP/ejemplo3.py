from abc import ABC, abstractmethod


class Entrega(ABC):
    @abstractmethod
    def calcular_costo(self, distancia: float) -> float:
        pass


class EntregaTerrestre(Entrega):
    def calcular_costo(self, distancia: float) -> float:
        if distancia < 0:
            raise ValueError("La distancia no puede ser negativa")

        return distancia * 2


class EntregaAerea(Entrega):
    def calcular_costo(self, distancia: float) -> float:
        if distancia < 0:
            raise ValueError("La distancia no puede ser negativa")

        return distancia * 5


class EntregaMaritima(Entrega):
    def calcular_costo(self, distancia: float) -> float:
        if distancia < 0:
            raise ValueError("La distancia no puede ser negativa")

        return distancia * 1.5


def mostrar_costo(entrega: Entrega, distancia: float) -> None:
    costo = entrega.calcular_costo(distancia)
    print(f"Costo de entrega: S/ {costo:.2f}")


mostrar_costo(EntregaTerrestre(), 100)
mostrar_costo(EntregaAerea(), 100)
mostrar_costo(EntregaMaritima(), 100)
