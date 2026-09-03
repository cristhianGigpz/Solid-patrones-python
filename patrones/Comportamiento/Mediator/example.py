class ChatMediator:
    def __init__(self):
        self.usuarios = []

    def agregar(self, usuario):
        self.usuarios.append(usuario)

    def enviar(self, mensaje, emisor):
        for usuario in self.usuarios:
            if usuario != emisor:
                usuario.recibir(mensaje, emisor)


class Usuario:
    def __init__(self, nombre, chat):
        self.nombre = nombre
        self.chat = chat

    def enviar(self, mensaje):
        self.chat.enviar(mensaje, self)

    def recibir(self, mensaje, emisor):
        print(f"{emisor.nombre}: {mensaje}")


chat = ChatMediator()

ana = Usuario("Ana", chat)
carlos = Usuario("Carlos", chat)
pedro = Usuario("Pedro", chat)

chat.agregar(ana)
chat.agregar(carlos)
chat.agregar(pedro)

ana.enviar("Hola a todos")

"""
class Usuario:

    def enviar(self):
        pedro.recibir()
        ana.recibir()
        maria.recibir()

        class Usuario:

    def enviar(self, mensaje):
        self.chat.enviar(
            mensaje,
            self
        )

"""
