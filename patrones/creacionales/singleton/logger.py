class Logger:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)

        return cls._instancia

    def log(self, mensaje):
        print(f"[LOG] {mensaje}")


logger1 = Logger()
logger2 = Logger()

logger1.log("Usuario registrado")
logger2.log("Pedido creado")

print(logger1 is logger2)
