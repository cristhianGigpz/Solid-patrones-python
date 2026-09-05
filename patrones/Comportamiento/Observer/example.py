from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def actualizar(self, mensaje):
        pass


class EmailObserver(Observer):
    def actualizar(self, mensaje):
        print(f"Email: {mensaje}")


class SMSObserver(Observer):
    def actualizar(self, mensaje):
        print(f"SMS: {mensaje}")


class WhatsAppObserver(Observer):
    def actualizar(self, mensaje):
        print(f"WhatsApp: {mensaje}")


class Producto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.observers = []
        self.stock = 0

    def suscribir(self, observer):
        self.observers.append(observer)

    def desuscribir(self, observer):
        self.observers.remove(observer)

    def cambiar_stock(self, stock):
        self.stock = stock
        if stock > 0:
            self.notificar(f"El producto {self.nombre} está disponible en stock.")

    def notificar(self, mensaje):
        for observer in self.observers:
            observer.actualizar(mensaje)


producto = Producto("PlayStation")

email = EmailObserver()
sms = SMSObserver()
whatsapp = WhatsAppObserver()

producto.suscribir(email)
producto.suscribir(sms)
producto.suscribir(whatsapp)

producto.notificar("PlayStation disponible")

producto.desuscribir(sms)

producto.notificar("Nuevo stock disponible")

producto.cambiar_stock(10)
