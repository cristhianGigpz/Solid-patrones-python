class Inventario:
    def verificar(self):
        print("Stock disponible")


class Pago:
    def procesar(self):
        print("Pago procesado")


class Envio:
    def preparar(self):
        print("Envío preparado")


class Email:
    def enviar(self):
        print("Email enviado")


class CheckoutFacade:
    # def __init__(self):
    #     self.inventario = Inventario()
    #     self.pago = Pago()
    #     self.envio = Envio()
    #     self.email = Email()
    def __init__(self, inventario, pago, envio, notificador):
        self.inventario = inventario
        self.pago = pago
        self.envio = envio
        self.notificador = notificador

    def comprar(self):
        self.inventario.verificar()
        self.pago.procesar()
        self.envio.preparar()
        self.email.enviar()


# inventario = Inventario()
# pago = Pago()
# envio = Envio()
# email = Email()

# inventario.verificar()
# pago.procesar()
# envio.preparar()
# email.enviar()
checkout = CheckoutFacade(Inventario(), Pago(), Envio(), Email())

checkout.comprar()
