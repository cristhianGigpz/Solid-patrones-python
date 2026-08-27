class ImagenReal:
    def __init__(self, archivo):
        print("Cargando imagen...")
        self.archivo = archivo

    def mostrar(self):
        print(self.archivo)


class ImagenProxy:
    def __init__(self, archivo):
        self.archivo = archivo
        self.imagen = None

    def mostrar(self):

        if self.imagen is None:
            self.imagen = ImagenReal(self.archivo)

        self.imagen.mostrar()


imagen = ImagenProxy("foto.jpg")
imagen.mostrar()
