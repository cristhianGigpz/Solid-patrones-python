from abc import ABC, abstractmethod


class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass


class Email(Notificacion):
    def enviar(self, mensaje):
        print(f"Email: {mensaje}")


class SMS(Notificacion):
    def enviar(self, mensaje):
        print(f"SMS: {mensaje}")


class WhatsApp(Notificacion):
    def enviar(self, mensaje):
        print(f"WhatsApp: {mensaje}")


###########################################################


class CreadorNotificacion(ABC):
    @abstractmethod
    def crear_notificacion(self):
        pass

    def notificar(self, mensaje):
        notificacion = self.crear_notificacion()
        notificacion.enviar(mensaje)


class CreadorEmail(CreadorNotificacion):
    def crear_notificacion(self):
        return Email()


class CreadorSMS(CreadorNotificacion):
    def crear_notificacion(self):
        return SMS()


class CreadorWhatsApp(CreadorNotificacion):
    def crear_notificacion(self):
        return WhatsApp()


# tipo = "email"


# if tipo == "email":
#     notificacion = NotificacionEmail()


# elif tipo == "sms":
#     notificacion = NotificacionSMS()


# notificacion.enviar("Pedido confirmado")
creador: CreadorNotificacion = CreadorEmail()


creador.notificar("Tu pedido fue confirmado")

creador = CreadorSMS()


creador.notificar("Tu pedido fue confirmado")

creador = CreadorWhatsApp()

creador.notificar("Tu pedido fue confirmado")
