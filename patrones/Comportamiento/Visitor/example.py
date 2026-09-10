from abc import ABC, abstractmethod


class Elemento(ABC):
    @abstractmethod
    def aceptar(self, visitor):
        pass


class Producto(Elemento):
    def __init__(self, precio):
        self.precio = precio

    def aceptar(self, visitor):
        return visitor.visitar_producto(self)


class Servicio(Elemento):
    def __init__(self, precio):
        self.precio = precio

    def aceptar(self, visitor):
        return visitor.visitar_servicio(self)


class Visitor(ABC):
    @abstractmethod
    def visitar_producto(self, producto):
        pass

    @abstractmethod
    def visitar_servicio(self, servicio):
        pass


class ImpuestoVisitor(Visitor):
    def visitar_producto(self, producto):
        return producto.precio * 0.18

    def visitar_servicio(self, servicio):
        return servicio.precio * 0.10


class ReporteVisitor(Visitor):
    def visitar_producto(self, producto):
        return f"Producto: S/{producto.precio}"

    def visitar_servicio(self, servicio):
        return f"Servicio: S/{servicio.precio}"


# producto = Producto(100)
# servicio = Servicio(200)

# impuestos = ImpuestoVisitor()

# print(producto.aceptar(impuestos))

# print(servicio.aceptar(impuestos))

# reporte = ReporteVisitor()

# print(producto.aceptar(reporte))
# print(servicio.aceptar(reporte))

elementos = [Producto(100), Servicio(200), Producto(50)]

visitor = ImpuestoVisitor()

for elemento in elementos:
    impuesto = elemento.aceptar(visitor)
    print(impuesto)
