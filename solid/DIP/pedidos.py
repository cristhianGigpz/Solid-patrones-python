from abc import ABC, abstractmethod


class PedidoRepository(ABC):
    @abstractmethod
    def guardar(self, pedido):
        pass


class ProcesadorPago(ABC):
    @abstractmethod
    def pagar(self, monto):
        pass


class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensaje):
        pass


###############################################################


class MySQLPedidoRepository(PedidoRepository):
    def guardar(self, pedido):
        print(f"Guardando {pedido} en MySQL")


class PostgreSQLPedidoRepository(PedidoRepository):
    def guardar(self, pedido):
        print(f"Guardando {pedido} en PostgreSQL")


###############################################################


class PayPalProcesador(ProcesadorPago):
    def pagar(self, monto):
        print(f"Procesando S/ {monto} con PayPal")


class YapeProcesador(ProcesadorPago):
    def pagar(self, monto):
        print(f"Procesando S/ {monto} con Yape")


###############################################################


class EmailNotificador(Notificador):
    def enviar(self, mensaje):
        print(f"Email enviado: {mensaje}")


class SMSNotificador(Notificador):
    def enviar(self, mensaje):
        print(f"SMS enviado: {mensaje}")


###############################################################


class PedidoService:
    def __init__(
        self,
        repositorio: PedidoRepository,
        pago: ProcesadorPago,
        notificador: Notificador,
    ):
        self.repositorio = repositorio
        self.pago = pago
        self.notificador = notificador

    def crear(self, pedido: str, total: float) -> None:

        self.pago.pagar(total)

        self.repositorio.guardar(pedido)

        self.notificador.enviar("Pedido creado correctamente")


repositorio = MySQLPedidoRepository()

pago = PayPalProcesador()

notificador = EmailNotificador()

servicio = PedidoService(repositorio, pago, notificador)

#############################################################

servicio.crear("Pedido #100", 250)

servicio = PedidoService(
    PostgreSQLPedidoRepository(), YapeProcesador(), SMSNotificador()
)
servicio.crear("Pedido #100", 250)


def crear_aplicacion():

    repositorio = PostgreSQLPedidoRepository()

    pago = YapeProcesador()

    notificador = SMSNotificador()

    return PedidoService(repositorio, pago, notificador)
