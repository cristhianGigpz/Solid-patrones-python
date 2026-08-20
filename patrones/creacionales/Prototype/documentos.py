import copy


class Documento:
    def __init__(self, titulo, formato):
        self.titulo = titulo
        self.formato = formato

    def clonar(self):
        return copy.deepcopy(self)


plantilla = Documento("Reporte", "A4")

reporte1 = plantilla.clonar()
reporte2 = plantilla.clonar()


reporte1.titulo = "Reporte de ventas"
reporte2.titulo = "Reporte financiero"
