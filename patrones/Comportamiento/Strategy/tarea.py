from abc import ABC, abstractmethod


class EstrategiaEnvio(ABC):
    @abstractmethod
    def calcular(self, peso):
        pass


class EnvioNormal(EstrategiaEnvio):
    def calcular(self, peso):
        return peso * 5


class EnvioExpress(EstrategiaEnvio):
    def calcular(self, peso):
        return peso * 10


class EnvioInternacional(EstrategiaEnvio):
    def calcular(self, peso):
        return peso * 20


class CalculadoraEnvio:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def cambiar_estrategia(self, estrategia):
        self.estrategia = estrategia

    def calcular(self, peso):
        return self.estrategia.calcular(peso)


envio = CalculadoraEnvio(EnvioExpress())
print(envio.calcular(3))

envio.cambiar_estrategia(EnvioNormal())
print(envio.calcular(3))

envio.cambiar_estrategia(EnvioInternacional())
print(envio.calcular(3))
