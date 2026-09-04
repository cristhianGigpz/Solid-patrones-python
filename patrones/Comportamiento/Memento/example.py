class EditorMemento:
    def __init__(self, texto):
        self._texto = texto

    def obtener_estado(self):
        return self._texto


class Editor:
    def __init__(self):
        self.texto = ""

    def escribir(self, texto):
        self.texto += texto

    def guardar(self):
        return EditorMemento(self.texto)

    def restaurar(self, memento):
        self.texto = memento.obtener_estado()


class Historial:
    def __init__(self):
        self.estados = []

    def guardar(self, memento):
        self.estados.append(memento)

    def deshacer(self):
        if self.estados:
            return self.estados.pop()


editor = Editor()
historial = Historial()

historial.guardar(editor.guardar())

editor.escribir("Hola ")

historial.guardar(editor.guardar())

editor.escribir("Mundo")

print(editor.texto)

estado = historial.deshacer()
editor.restaurar(estado)

print(editor.texto)
