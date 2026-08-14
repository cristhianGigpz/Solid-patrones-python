from abc import ABC, abstractmethod


class Documento(ABC):
    @abstractmethod
    def abrir(self):
        pass


class PDF(Documento):
    def abrir(self):
        print("Abriendo PDF")


class Excel(Documento):
    def abrir(self):
        print("Abriendo Excel")


########################################
class CreadorDocumento(ABC):
    @abstractmethod
    def crear(self):
        pass


class CreadorPDF(CreadorDocumento):
    def crear(self):
        return PDF()


class CreadorExcel(CreadorDocumento):
    def crear(self):
        return Excel()


########################################

creador: CreadorDocumento = CreadorPDF()


documento = creador.crear()

documento.abrir()

creador = CreadorExcel()

documento = creador.crear()

documento.abrir()
