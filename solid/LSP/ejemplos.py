from abc import ABC, abstractmethod


class Figura(ABC):
    @abstractmethod
    def calcular_area(self) -> float:
        pass


class Rectangulo(Figura):
    def __init__(self, ancho: float, alto: float):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self) -> float:
        return self.ancho * self.alto


class Cuadrado(Figura):
    def __init__(self, lado: float):
        self.lado = lado

    def calcular_area(self) -> float:
        return self.lado**2


def mostrar_area(figura: Figura) -> None:
    print(figura.calcular_area())


mostrar_area(Rectangulo(5, 4))
mostrar_area(Cuadrado(4))

# Precondiciones
# class ProcesadorPago:
#     def pagar(self, monto: float) -> None:
#         if monto <= 0:
#             raise ValueError("El monto debe ser mayor que cero")

#         print(f"Procesando pago de {monto}")


# class PagoPremium(ProcesadorPago):
#     def pagar(self, monto: float) -> None:
#         if monto < 100:
#             raise ValueError("El monto mínimo es 100")

#         print(f"Procesando pago premium de {monto}")

# Postcondiciones
# class Convertidor:
#     def convertir(self, texto: str) -> str:
#         return texto.upper()


# class ConvertidorEspecial(Convertidor):
#     def convertir(self, texto: str) -> None:
#         print(texto.upper())


# def procesar(convertidor: Convertidor):
#     resultado = convertidor.convertir("hola")
#     print(resultado.lower())


# Invariantes
class Cuenta:
    def __init__(self, saldo: float):
        if saldo < 0:
            raise ValueError("El saldo no puede ser negativo")

        self.saldo = saldo


class CuentaEspecial(Cuenta):
    def establecer_saldo(self, saldo: float):
        self.saldo = saldo


cuenta = CuentaEspecial(100)
cuenta.establecer_saldo(-500)


# class Archivo:
#     def guardar(self):
#         print("Guardando archivo")

#     def eliminar(self):
#         print("Eliminando archivo")


# class ArchivoSoloLectura(Archivo):
#     def eliminar(self):
#         raise PermissionError("Este archivo no puede eliminarse")
class Almacenamiento:
    def guardar(self):
        print("Guardando archivo")


class ArchivoSoloLectura:
    def __init__(self, almacenamiento: Almacenamiento):
        self.almacenamiento = almacenamiento

    def guardar(self):
        self.almacenamiento.guardar()
