class Notificador:
    def enviar(self, mensaje):
        print(f"Email: {mensaje}")


class NotificadorSMS:
    def __init__(self, notificador):
        self.notificador = notificador

    def enviar(self, mensaje):
        self.notificador.enviar(mensaje)
        print(f"SMS: {mensaje}")


class NotificadorWhatsApp:
    def __init__(self, notificador):
        self.notificador = notificador

    def enviar(self, mensaje):
        self.notificador.enviar(mensaje)
        print(f"WhatsApp: {mensaje}")


# notificador = Notificador()


# notificadorSMS = NotificadorSMS(notificador)


# notificadorWhatsApp = NotificadorWhatsApp(notificadorSMS)


# notificadorWhatsApp.enviar("Pedido confirmado")
notificador = NotificadorWhatsApp(NotificadorSMS(Notificador()))
notificador.enviar("Pedido confirmado")
