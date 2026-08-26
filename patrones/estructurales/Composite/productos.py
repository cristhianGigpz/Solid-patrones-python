class Producto:
    def __init__(self, precio):
        self.precio = precio

    def obtener_precio(self):
        return self.precio


class Caja:
    def __init__(self):
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def obtener_precio(self):
        return sum(elemento.obtener_precio() for elemento in self.elementos)


manzana = Producto(1.5)
banana = Producto(2.0)

caja_frutas = Caja()
caja_frutas.agregar(manzana)
caja_frutas.agregar(banana)

print(caja_frutas.obtener_precio())
