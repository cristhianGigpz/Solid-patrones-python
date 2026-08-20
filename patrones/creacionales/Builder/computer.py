# class Computadora:
#     def __init__(self, cpu, ram, almacenamiento, gpu, wifi, bluetooth):
#         self.cpu = cpu
#         self.ram = ram
#         self.almacenamiento = almacenamiento
#         self.gpu = gpu
#         self.wifi = wifi
#         self.bluetooth = bluetooth


# pc = Computadora("Intel i7", "32GB", "1TB SSD", "RTX 5070", True, True)


class Computadora:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.almacenamiento = None
        self.gpu = None

    def __str__(self):
        return (
            f"CPU: {self.cpu}, "
            f"RAM: {self.ram}, "
            f"Disco: {self.almacenamiento}, "
            f"GPU: {self.gpu}"
        )


class ComputadoraBuilder:
    def __init__(self):
        self.computadora = Computadora()

    def agregar_cpu(self, cpu):
        self.computadora.cpu = cpu
        return self

    def agregar_ram(self, ram):
        self.computadora.ram = ram
        return self

    def agregar_almacenamiento(self, disco):
        self.computadora.almacenamiento = disco
        return self

    def agregar_gpu(self, gpu):
        self.computadora.gpu = gpu
        return self

    def construir(self):
        return self.computadora


class Director:
    def pc_gamer(self, builder):
        return (
            builder.agregar_cpu("Ryzen 9")
            .agregar_ram("32GB")
            .agregar_gpu("RTX 5080")
            .construir()
        )


builder1 = ComputadoraBuilder()
director = Director()

pc = director.pc_gamer(builder1)
print(pc)

builder = ComputadoraBuilder()

pc = (
    builder.agregar_cpu("Intel i7")
    .agregar_ram("32GB")
    .agregar_almacenamiento("1TB SSD")
    .agregar_gpu("RTX 5070")
    .construir()
)

print(pc)

pc_oficina = (
    ComputadoraBuilder()
    .agregar_cpu("Intel i5")
    .agregar_ram("16GB")
    .agregar_almacenamiento("512GB SSD")
    .construir()
)

print(pc_oficina)

pc_gamer = (
    ComputadoraBuilder()
    .agregar_cpu("Ryzen 9")
    .agregar_ram("32GB")
    .agregar_almacenamiento("2TB SSD")
    .agregar_gpu("RTX 5080")
    .construir()
)

print(pc_gamer)
