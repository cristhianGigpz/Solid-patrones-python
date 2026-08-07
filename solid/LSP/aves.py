class Ave:
    def comer(self):
        print("El ave está comiendo")


class AveVoladora(Ave):
    def volar(self):
        print("El ave está volando")


class Aguila(AveVoladora):
    pass


class Pinguino(Ave):
    pass


def alimentar(ave: Ave):
    ave.comer()


def hacer_volar(ave: AveVoladora):
    ave.volar()


alimentar(Aguila())
alimentar(Pinguino())
hacer_volar(Aguila())
# hacer_volar(Pinguino())  # Esto lanzará una excepción NotImplementedError

# if isinstance(ave, Pinguino):
#     ...
# else:
#     ave.volar()
