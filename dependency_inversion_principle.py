"""
The Dependency Inversion Principle (DIP) is an essential principle of object-oriented programming that emphasizes the need
to design software modules that are loosely coupled and independent. The DIP proposes that higher-level modules should rely
on abstractions rather than concrete implementations provided by lower-level modules.

To achieve this, the DIP encourages the use of interfaces or abstract classes as a way of creating a loosely-coupled
relationship between modules. Instead of creating a tightly-coupled relationship between modules, the abstraction acts
as a mediator that enables modules to interact without directly knowing each other's implementation details.

Following the Dependency Inversion Principle, modules can be developed and tested independently, making it easier to maintain
and extend the code base. Also, changes made to one module do not affect other modules as long as the abstraction remains
unchanged. Thus, this principle makes it possible to reuse modules in different contexts without modifying the code,
thus promoting code reusability.
"""

from abc import ABC, abstractmethod


class Topping(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass


class Mushroom(Topping):

    def get_name(self) -> str:
        return "Mushroom"


class Onion(Topping):

    def get_name(self) -> str:
        return "Onion"


class Pepperoni(Topping):

    def get_name(self) -> str:
        return "Pepperoni"


class Pizza(ABC):

    @abstractmethod
    def add_topping(self, topping: Topping) -> None:
        pass

    @abstractmethod
    def get_toppings(self) -> list[Topping]:
        pass


class VegPizza(Pizza):

    def __init__(self):
        self.toppings = []

    def add_topping(self, topping: Topping) -> None:
        self.toppings.append(topping)

    def get_toppings(self) -> list[Topping]:
        return self.toppings


class OrderProcessor:

    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    def process_order(self) -> None:
        toppings = self.pizza.get_toppings()
        print("Preparing pizza with toppings:")
        for topping in toppings:
            print("- " + topping.get_name())


def example():
    mushroom = Mushroom()
    onion = Onion()
    bell_pepper = Pepperoni()

    veg_pizza = VegPizza()
    veg_pizza.add_topping(mushroom)
    veg_pizza.add_topping(onion)
    veg_pizza.add_topping(bell_pepper)

    order_processor = OrderProcessor(veg_pizza)
    order_processor.process_order()


if __name__ == '__main__':
    example()
