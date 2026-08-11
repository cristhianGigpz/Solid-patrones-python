from typing import Protocol


class Notificador(Protocol):
    def enviar(self, mensaje: str) -> None: ...


class Email:
    def enviar(self, mensaje: str) -> None:

        print(f"Email: {mensaje}")


class PedidoService:
    def __init__(self, notificador: Notificador):
        self.notificador = notificador


# class MySQLInterface(ABC):
#     @abstractmethod
#     def ejecutar_sql(self):
#         pass


# class UsuarioService:
#     def __init__(self, mysql: MySQLInterface): ...

# class SistemaEmpresa(ABC):
#     def guardar_usuario(self): ...

#     def enviar_email(self): ...

#     def procesar_pago(self): ...

#     def generar_pdf(self): ...

#     def subir_archivo(self): ...

# UsuarioRepository
# Notificador
# ProcesadorPago
# GeneradorDocumento
# AlmacenamientoArchivo
