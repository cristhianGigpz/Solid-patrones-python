class BibliotecaIterator:
    def __init__(self, libros):
        self.libros = libros
        self.indice = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.indice >= len(self.libros):
            raise StopIteration

        libro = self.libros[self.indice]

        self.indice += 1

        return libro


class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar(self, libro):
        self.libros.append(libro)

    def __iter__(self):
        return BibliotecaIterator(self.libros)


biblioteca = Biblioteca()

biblioteca.agregar("Clean Code")
biblioteca.agregar("Design Patterns")

for libro in biblioteca:
    print(libro)
