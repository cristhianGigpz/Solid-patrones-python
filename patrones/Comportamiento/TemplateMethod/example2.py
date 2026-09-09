from abc import ABC, abstractmethod


class GeneradorReporte(ABC):
    def generar(self):
        self.obtener_datos()
        self.crear_archivo()

        if self.enviar_email():
            print("Enviando reporte por email")

    def obtener_datos(self):
        print("Obteniendo datos")

    @abstractmethod
    def crear_archivo(self):
        pass

    def enviar_email(self):
        return False


class ReportePDF(GeneradorReporte):
    def crear_archivo(self):
        print("Generando PDF")

    def enviar_email(self):
        return True


pdf = ReportePDF()
pdf.generar()
