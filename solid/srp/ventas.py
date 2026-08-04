class Venta:
    def calcular_total(self):
        print("Calculando total")

    def aplicar_descuento(self):
        print("Aplicando descuento")


class VentaRepository:
    def guardar(self, venta):
        print("Venta guardada")


class EmailService:
    def enviar_comprobante(self, venta):
        print("Correo enviado")


class FacturaPDF:
    def generar(self, venta):
        print("Factura generada")
