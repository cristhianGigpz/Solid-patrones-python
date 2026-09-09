from abc import ABC, abstractmethod


class GeneradorReporte(ABC):
    def generar(self):
        self.obtener_datos()
        self.procesar_datos()
        self.crear_archivo()
        self.guardar()

    def obtener_datos(self):
        print("Obteniendo datos")

    def procesar_datos(self):
        print("Procesando datos")

    @abstractmethod
    def crear_archivo(self):
        pass

    def guardar(self):
        print("Guardando reporte")


class ReportePDF(GeneradorReporte):
    def crear_archivo(self):
        print("Generando archivo PDF")


class ReporteExcel(GeneradorReporte):
    def crear_archivo(self):
        print("Generando archivo Excel")


class ReporteCSV(GeneradorReporte):
    def crear_archivo(self):
        print("Generando archivo CSV")


pdf = ReportePDF()
pdf.generar()
print("---------------------")
excel = ReporteExcel()
excel.generar()
print("---------------------")
csv = ReporteCSV()
csv.generar()
