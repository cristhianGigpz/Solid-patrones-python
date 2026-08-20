# {
#     "nombre": "Ana",
#     "email": "ana@email.com"
# }

# {
#     "first_name": "Ana",
#     "email_address": "ana@email.com"
# }
class UsuarioAdapter:
    def __init__(self, usuario_externo):
        self.usuario = usuario_externo

    def obtener(self):
        return {
            "nombre": self.usuario["first_name"],
            "email": self.usuario["email_address"],
        }
