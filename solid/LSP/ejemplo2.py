from typing import Protocol


class Reproducible(Protocol):
    def reproducir(self) -> None: ...


class Cancion:
    def reproducir(self) -> None:
        print("Reproduciendo canción")


class Podcast:
    def reproducir(self) -> None:
        print("Reproduciendo podcast")


def iniciar_reproduccion(contenido: Reproducible) -> None:
    contenido.reproducir()


iniciar_reproduccion(Cancion())
iniciar_reproduccion(Podcast())


# class PagoYape(MetodoPago):
#     def pagar(self, monto):
#         raise Exception("Este método todavía no está disponible")
