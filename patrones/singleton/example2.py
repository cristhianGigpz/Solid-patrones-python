class Configuracion:
    def __init__(self):
        self.debug = False


config = Configuracion()

# usuario_service = UsuarioService(config)
# pedido_service = PedidoService(config)


# class PedidoService:
#     def procesar(self):
#         config = Configuracion()


class PedidoService:
    def __init__(self, config):
        self.config = config
