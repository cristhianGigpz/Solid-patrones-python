class Aprobaciones:
    def __init__(self):
        self.siguiente = None

    def establecer_siguiente(self, aprobacion):
        self.siguiente = aprobacion
        return aprobacion

    def aprobar(self, monto):
        if self.siguiente:
            return self.siguiente.aprobar(monto)

        print("Se necesita de un ejecutivo de mas alto nivel para el Monto.")


class Supervisor(Aprobaciones):
    def aprobar(self, monto):
        if monto <= 500:
            print("Superviosor aprobó el gasto")
            return

        return super().aprobar(monto)


class Gerente(Aprobaciones):
    def aprobar(self, monto):
        if monto <= 5000:
            print("Gerente aprobó el gasto")
            return
        return super().aprobar(monto)


class Director(Aprobaciones):
    def aprobar(self, monto):
        if monto <= 20000:
            print("Director aprobó el gasto")
            return

        return super().aprobar(monto)


supervisor = Supervisor()
gerente = Gerente()
director = Director()

supervisor.establecer_siguiente(gerente).establecer_siguiente(director)

supervisor.aprobar(50000)
