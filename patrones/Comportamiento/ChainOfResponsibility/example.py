# def atender(problema):
#     if problema == "basico":
#         print("Soporte básico")
#     elif problema == "tecnico":
#         print("Soporte técnico")
#     elif problema == "critico":
#         print("Especialista")

"""
básico
técnico
crítico
seguridad
servidores
base de datos
"""


class Soporte:
    def __init__(self):
        self.siguiente = None

    def establecer_siguiente(self, soporte):
        self.siguiente = soporte
        return soporte

    def atender(self, problema):
        if self.siguiente:
            return self.siguiente.atender(problema)

        print("Problema no resuelto")


class SoporteBasico(Soporte):
    def atender(self, problema):
        if problema == "basico":
            print("Soporte básico resolvió el problema")
            return

        super().atender(problema)


class SoporteTecnico(Soporte):
    def atender(self, problema):
        if problema == "tecnico":
            print("Soporte técnico resolvió el problema")
            return

        super().atender(problema)


class SoporteSeguridad(Soporte):
    def atender(self, problema):
        if problema == "seguridad":
            print("Especialista en Seguridad resolvió el problema")
            return
        super().atender(problema)


class Especialista(Soporte):
    def atender(self, problema):
        if problema == "critico":
            print("Especialista resolvió el problema")
            return

        super().atender(problema)


basico = SoporteBasico()
tecnico = SoporteTecnico()
seguridad = SoporteSeguridad()
especialista = Especialista()

basico.establecer_siguiente(tecnico).establecer_siguiente(
    seguridad
).establecer_siguiente(especialista)


# basico.atender("tecnico")
# basico.atender("critico")
basico.atender("seguridad")
##basico.atender("desconocido")
