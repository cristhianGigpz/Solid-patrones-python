class Pedido:
    def calcular_total(self):
        print("Calculando total")


# (Repositorio)
class PedidoRepository:
    def guardar(self, pedido):
        print("Guardando pedido")


# (Servicio de correo)
class EmailService:
    def enviar(self, pedido):
        print("Enviando email")


# (Generador de PDF)
class PDFGenerator:
    def generar(self, pedido):
        print("Generando PDF")
