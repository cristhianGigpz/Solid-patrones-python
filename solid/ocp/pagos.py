from abc import ABC, abstractmethod


class MetodoPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass


class PagoEfectivo(MetodoPago):
    def pagar(self, monto):
        print(f"Pago en efectivo: ${monto}")


class PagoTarjeta(MetodoPago):
    def pagar(self, monto):
        print(f"Pago con tarjeta: ${monto}")


class PagoPaypal(MetodoPago):
    def pagar(self, monto):
        print(f"Pago con PayPal: ${monto}")


class PagoYape(MetodoPago):
    def pagar(self, monto):
        print(f"Pago con Yape: ${monto}")


# def procesar_pago(tipo):
#     if tipo == "efectivo":
#         print("Pago en efectivo")
#     elif tipo == "tarjeta":
#         print("Pago con tarjeta")
def procesar_pago(metodo, monto):
    metodo.pagar(monto)


procesar_pago(PagoEfectivo(), 150)

procesar_pago(PagoTarjeta(), 200)

procesar_pago(PagoPaypal(), 500)

procesar_pago(PagoYape(), 1000)
