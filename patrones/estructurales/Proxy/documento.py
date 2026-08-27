class Documento:
    def eliminar(self):
        print("Documento eliminado")


class DocumentoProxy:
    def __init__(self, documento, usuario):
        self.documento = documento
        self.usuario = usuario

    def eliminar(self):

        if self.usuario != "admin":
            print("Acceso denegado")
            return

        self.documento.eliminar()


documento = Documento()

proxy = DocumentoProxy(documento, "invitado")

proxy.eliminar()

proxy = DocumentoProxy(documento, "admin")

proxy.eliminar()
