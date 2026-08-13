# class PedidoService:
#     def procesar(self):
#         logger = Logger()
#         logger.log("Procesando pedido")


class Configuracion:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)

        return cls._instancia

    def __init__(self):
        self.debug = False
        self.idioma = "es"


config1 = Configuracion()
config1.debug = True
config1.idioma = "es"

config2 = config1

print(config2.debug)
print(config2.idioma)
##config1.debug = True
##print(config2.debug)
##print(config1 is config2)
