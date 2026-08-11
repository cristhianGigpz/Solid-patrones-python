# from abc import ABC, abstractmethod


# class Notificador(ABC):
#     @abstractmethod
#     def enviar(self, mensaje: str) -> None:
#         pass


# class EmailNotificador(Notificador):
#     def enviar(self, mensaje: str) -> None:
#         print(f"Email: {mensaje}")


# class SMSNotificador(Notificador):
#     def enviar(self, mensaje: str) -> None:
#         print(f"SMS: {mensaje}")


# class WhatsAppNotificador(Notificador):
#     def enviar(self, mensaje: str) -> None:
#         print(f"WhatsApp: {mensaje}")


# class PedidoService:
#     def __init__(self, notificador: Notificador):
#         self.notificador = notificador

#     def crear_pedido(self) -> None:
#         print("Pedido creado")

#         self.notificador.enviar("Tu pedido fue confirmado")


# servicio = PedidoService(EmailNotificador())

# servicio.crear_pedido()

# servicio = PedidoService(SMSNotificador())
# servicio.crear_pedido()

# servicio = PedidoService(WhatsAppNotificador())
# servicio.crear_pedido()


# class ReporteService:
#     def generar(self, exportador):
#         exportador.exportar()


# reporte = ReporteService()


# reporte.generar(PDFExporter())

# class Servicio:
#     def __init__(self):
#         self.notificador = None


# servicio = Servicio()


# servicio.notificador = EmailNotificador()
class PedidoServices:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def crear(self, pedido):
        self.repositorio.guardar(pedido)


class RepositorioMemoria:
    def __init__(self):
        self.pedidos = []

    def guardar(self, pedido):
        self.pedidos.append(pedido)


repositorio = RepositorioMemoria()

servicio = PedidoServices(repositorio)

servicio.crear("Pedido #1")
