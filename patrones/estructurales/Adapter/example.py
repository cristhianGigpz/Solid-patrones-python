class ProcesadorPago:
    def pagar(self, monto):
        pass


class PayPal(ProcesadorPago):
    def pagar(self, monto):
        print(f"PayPal: S/ {monto}")


class StripeAPI:
    def make_payment(self, amount):
        print(f"Stripe: S/ {amount}")


class StripeAdapter(ProcesadorPago):
    def __init__(self, stripe):
        self.stripe = stripe

    def pagar(self, monto):
        self.stripe.make_payment(monto)


# procesador = PayPal()
# procesador.pagar(100)

# stripe = StripeAPI()
# procesador = StripeAdapter(stripe)
# procesador.pagar(100)


class CompraService:
    def __init__(self, pago):
        self.pago = pago

    def comprar(self, monto):
        self.pago.pagar(monto)


stripe = StripeAdapter(StripeAPI())
compra_service = CompraService(stripe)
compra_service.comprar(100)
