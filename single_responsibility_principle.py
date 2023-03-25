"""
The Single Responsibility Principle (SRP) is one of object-oriented programming principles, which emphasizes that a class should have only one responsibility
or job. The purpose of this principle is to ensure that classes are designed with a well-defined responsibility that they can execute perfectly.

To achieve the SRP, a class should be designed to have a clear and focused responsibility, and it should not try to do too much. In cases where a class has
multiple responsibilities, it should be divided into smaller, more specialized classes, each with a single responsibility. These can be accomplished through
techniques such as abstraction, composition, and delegation.

In conclusion, adhering to the Single Responsibility Principle (SRP) guarantees that code is maintainable, flexible, and reusable. Additionally, it reduces
the possibility of introducing bugs or errors in unrelated parts of the code.
"""


from dataclasses import dataclass
from math import pi


@dataclass
class Topping:
    name: str
    price: float

    def __str__(self) -> str:
        return self.name


class Pizza:

    def __init__(self, toppings: list[Topping], radius: int):
        self.toppings = toppings
        self.radius = radius

    @property
    def area(self) -> float:
        return self.radius ** 2 * pi

    def __str__(self) -> str:
        return f"Pizza with: {', '.join(str(topping) for topping in self.toppings)}; size: {self.radius}cm"

    def calculate_cost(self) -> float:
        return 0.0015 * self.area + sum(topping.price * self.radius for topping in self.toppings)


class PizzaOrder:

    def __init__(self, pizzas: list[Pizza], delivery_cost: float):
        self.pizzas = pizzas
        self.delivery_cost = delivery_cost

    @property
    def total_price(self) -> float:
        return round(sum(pizza.calculate_cost() for pizza in self.pizzas) + self.delivery_cost, 2)

    def print_order(self) -> None:
        separator = '\n\t- '
        pizzas = separator.join(str(pizza) for pizza in self.pizzas)
        cost = self.total_price
        print(f"Your order:{separator}{pizzas}\nTotal costs: ${cost}")


def example() -> None:
    cheese = Topping('cheese', 0.06)
    mushrooms = Topping('mushrooms', 0.1)
    pepperoni = Topping('pepperoni', 0.18)
    jalapeno = Topping('jalapeno', 0.14)
    ham = Topping('ham', 0.08)

    pepperoni_pizza = Pizza([cheese, mushrooms, pepperoni], 42)
    diabola_pizza = Pizza([cheese, pepperoni, jalapeno], 28)
    home_pizza = Pizza([cheese, ham], 32)

    order = PizzaOrder([pepperoni_pizza, diabola_pizza, home_pizza], 3.49)
    order.print_order()


if __name__ == '__main__':
    example()
