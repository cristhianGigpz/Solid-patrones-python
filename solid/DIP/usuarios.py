from abc import ABC, abstractmethod


# class UsuarioService:
#     def __init__(self):
#         self.repositorio = MySQLUsuarioRepository()
class UsuarioRepository(ABC):
    @abstractmethod
    def guardar(self, nombre: str) -> None:
        pass


class MySQLUsuarioRepository(UsuarioRepository):
    def guardar(self, nombre: str) -> None:
        print(f"Guardando {nombre} en MySQL")


class PostgreSQLUsuarioRepository(UsuarioRepository):
    def guardar(self, nombre: str) -> None:
        print(f"Guardando {nombre} en PostgreSQL")


class UsuarioService:
    def __init__(self, repositorio: UsuarioRepository):
        self.repositorio = repositorio

    def registrar(self, nombre: str) -> None:
        self.repositorio.guardar(nombre)

        print(f"Usuario {nombre} registrado")


# repositorio = MySQLUsuarioRepository()

# servicio = UsuarioService(repositorio)

# servicio.registrar("Cristian")

repositorio = PostgreSQLUsuarioRepository()

servicio = UsuarioService(repositorio)

servicio.registrar("Cristian")
