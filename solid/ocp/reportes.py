from abc import ABC, abstractmethod


class Exportador(ABC):
    @abstractmethod
    def exportar(self):
        pass


# def exportar(tipo):


#     if tipo == "pdf":
#         print("PDF")
class PDFExporter(Exportador):
    def exportar(self):
        print("Exportando PDF")


class WordExporter(Exportador):
    def exportar(self):
        print("Exportando Word")


class CSVExporter(Exportador):
    def exportar(self):
        print("Exportando CSV")


def generar(exportador):
    exportador.exportar()


generar(PDFExporter())

generar(WordExporter())
