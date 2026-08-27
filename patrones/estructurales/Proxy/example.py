from abc import ABC, abstractmethod


class ServicioUsuarios(ABC):
    @abstractmethod
    def obtener_usuario(self, id):
        pass


class ApiUsuarios(ServicioUsuarios):
    def obtener_usuario(self, id):
        print("Consultando API...")

        return {"id": id, "nombre": "Ana"}


class UsuariosProxy(ServicioUsuarios):
    def __init__(self, servicio):
        self.servicio = servicio
        self.cache = {}

    def obtener_usuario(self, id):

        if id not in self.cache:
            self.cache[id] = self.servicio.obtener_usuario(id)

        return self.cache[id]


api = ApiUsuarios()

servicio = UsuariosProxy(api)

print(servicio.obtener_usuario(1))
print("=========================")
print(servicio.obtener_usuario(1))
print("=========================")
print("=========================")
print(servicio.obtener_usuario(2))
print("=========================")
print(servicio.obtener_usuario(2))
