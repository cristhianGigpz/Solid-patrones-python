from abc import ABC, abstractmethod


class EstrategiaPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass


class PagoTarjeta(EstrategiaPago):
    def pagar(self, monto):
        print(f"Pagando S/{monto} con tarjeta")


class PagoPayPal(EstrategiaPago):
    def pagar(self, monto):
        print(f"Pagando S/{monto} con PayPal")


class PagoTransferencia(EstrategiaPago):
    def pagar(self, monto):
        print(f"Pagando S/{monto} por transferencia")


class PagoYape(EstrategiaPago):
    def pagar(self, monto):
        print(f"Pagando S/{monto} con Yape")


class ProcesadorPago:
    def __init__(self, estrategia):
        self.estrategia = estrategia

    def cambiar_estrategia(self, estrategia):
        self.estrategia = estrategia

    def pagar(self, monto):
        self.estrategia.pagar(monto)


procesador = ProcesadorPago(PagoTarjeta())
procesador.pagar(200)

# procesador = ProcesadorPago(PagoPayPal())
procesador.cambiar_estrategia(PagoPayPal())
procesador.pagar(100)

procesador = ProcesadorPago(PagoYape())

procesador.pagar(50)
