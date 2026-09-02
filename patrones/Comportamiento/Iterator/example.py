class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar(self, libro):
        self.libros.append(libro)

    def __iter__(self):
        return iter(self.libros)

    def inverso(self):
        return reversed(self.libros)


biblioteca = Biblioteca()

biblioteca.agregar("Clean Code")
biblioteca.agregar("Design Patterns")

for libro in biblioteca:
    print(libro)

for libro in biblioteca.inverso():
    print(libro)

lista = [10, 20, 30]

# iterador = iter(lista)
iterador = iter([10, 20, 30])
print(next(iterador))
print(next(iterador))
