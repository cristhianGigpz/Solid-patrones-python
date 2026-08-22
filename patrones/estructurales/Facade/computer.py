class CPU:
    def iniciar(self):
        print("CPU iniciada")


class Memoria:
    def cargar(self):
        print("Memoria cargada")


class Disco:
    def leer(self):
        print("Sistema operativo cargado")


class ComputadoraFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memoria = Memoria()
        self.disco = Disco()

    def encender(self):
        self.cpu.iniciar()
        self.memoria.cargar()
        self.disco.leer()

    def reiniciar(self):
        self.apagar()
        self.encender()

    def apagar(self):
        print("Computadora apagada")


# cpu = CPU()
# memoria = Memoria()
# disco = Disco()

# cpu.iniciar()
# memoria.cargar()
# disco.leer()
computadora = ComputadoraFacade()

computadora.encender()
computadora.apagar()
