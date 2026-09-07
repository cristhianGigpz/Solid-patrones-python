from abc import ABC, abstractmethod


class EstadoPedido(ABC):
    @abstractmethod
    def avanzar(self, pedido):
        pass


class Pendiente(EstadoPedido):
    def avanzar(self, pedido):
        print("Pedido pagado")

        pedido.cambiar_estado(Pagado())

    def cancelar(self, pedido):
        print("Pedido cancelado")


class Pagado(EstadoPedido):
    def avanzar(self, pedido):
        print("Pedido enviado")

        pedido.cambiar_estado(Enviado())


class Enviado(EstadoPedido):
    def avanzar(self, pedido):
        print("Pedido entregado")

        pedido.cambiar_estado(Entregado())


class Entregado(EstadoPedido):
    def avanzar(self, pedido):
        print("El pedido ya fue entregado")

    def cancelar(self, pedido):
        print("No se puede cancelar")


class Pedido:
    def __init__(self):
        self.estado = Pendiente()

    def cambiar_estado(self, estado):
        self.estado = estado

    def avanzar(self):
        self.estado.avanzar(self)


pedido = Pedido()
pedido.avanzar()
pedido.avanzar()
pedido.avanzar()
