class TorreControl:
    def __init__(self):
        self.aviones = []

    def registrar_avion(self, avion):
        self.aviones.append(avion)

    def enviar_mensaje(self, mensaje, avion):
        for a in self.aviones:
            if a != avion:
                print(f"Mensaje de {avion.nombre} a {a.nombre}: {mensaje}")


class Avion:
    def __init__(self, nombre, torre):
        self.nombre = nombre
        self.torre = torre

    def enviar_mensaje(self, mensaje):
        self.torre.enviar_mensaje(mensaje, self)


torre = TorreControl()

avion1 = Avion("Avión 1", torre)
avion2 = Avion("Avión 2", torre)
avion3 = Avion("Avión 3", torre)

torre.registrar_avion(avion1)
torre.registrar_avion(avion2)
torre.registrar_avion(avion3)

avion1.enviar_mensaje("Solicito permiso para aterrizar.")
