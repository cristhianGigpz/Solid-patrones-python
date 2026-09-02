class Contador:
    def __init__(self, limite):
        self.actual = 1
        self.limite = limite

    def __iter__(self):
        return self

    def __next__(self):

        if self.actual > self.limite:
            raise StopIteration

        numero = self.actual
        self.actual += 1

        return numero


for numero in Contador(5):
    print(numero)


def contador(limite):
    yield from range(1, limite + 1)


for numero in contador(5):
    print(numero)
