class Editor:
    def escribir(self, texto):
        print(f"Escribiendo: {texto}")

    def borrar(self):
        print("Borrando texto")


class EscribirCommand:
    def __init__(self, editor, texto):
        self.editor = editor
        self.texto = texto

    def ejecutar(self):
        self.editor.escribir(self.texto)

    def deshacer(self):
        self.editor.borrar()


class BorrarCommand:
    def __init__(self, editor):
        self.editor = editor

    def ejecutar(self):
        self.editor.borrar()

    def deshacer(self):
        print("Deshaciendo borrado")


class EditorInvoker:
    def __init__(self):
        self.historial = []

    def ejecutar(self, comando):
        comando.ejecutar()
        self.historial.append(comando)

    def deshacer(self):
        if self.historial:
            comando = self.historial.pop()
            comando.deshacer()


editor = Editor()
escribir = EscribirCommand(editor, "Hola mundo")
borrar = BorrarCommand(editor)


invoker = EditorInvoker()
invoker.ejecutar(escribir)
invoker.ejecutar(borrar)
