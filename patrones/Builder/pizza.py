class Pizza:
    def __init__(self):
        self.ingredientes = []

    def __str__(self):
        return ", ".join(self.ingredientes)


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def agregar_queso(self):
        self.pizza.ingredientes.append("queso")
        return self

    def agregar_jamon(self):
        self.pizza.ingredientes.append("jamón")
        return self

    def agregar_aceitunas(self):
        self.pizza.ingredientes.append("aceitunas")
        return self

    def agregar_pina(self):
        self.pizza.ingredientes.append("piña")
        return self

    def construir(self):
        return self.pizza


pizza_americana = (
    PizzaBuilder().agregar_queso().agregar_jamon().agregar_aceitunas().construir()
)
print(pizza_americana)

pizza_hawai = (
    PizzaBuilder()
    .agregar_queso()
    .agregar_jamon()
    .agregar_aceitunas()
    .agregar_pina()
    .construir()
)
print(pizza_hawai)
