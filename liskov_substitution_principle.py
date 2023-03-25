"""
The Liskov Substitution Principle (LSP) is a crucial aspect of object-oriented programming, which suggests that a subclass should be used
in place of its superclass without changing the correctness of the program. In simpler terms, the subclass should be able to substitute
the superclass without causing any unexpected behavior.

To follow the LSP, the subclass must comply with the contract established by its superclass. This implies that the subclass should implement
all of the superclass's methods and behave similarly in all situations. If the subclass cannot conform to the contract, it indicates that it
is not a true subtype of the superclass and should not be used as a substitute.

By adhering to the Liskov Substitution Principle, code can be created to be more flexible and adaptable to change. It also makes it simpler
to reuse existing code and to develop new features by building on top of established classes and interfaces.
"""


class Pizza:

    def __init__(self, size: int):
        self.size = size

    def get_size(self) -> int:
        return self.size

    def get_toppings(self) -> list[str]:
        raise NotImplementedError("Method Pizza.get_toppings() not implemented.")


class CheesePizza(Pizza):

    def get_toppings(self) -> list[str]:
        return ["cheese"]


class PepperoniPizza(Pizza):

    def get_toppings(self) -> list[str]:
        return ["cheese", "pepperoni"]


class CustomPizza(Pizza):

    def __init__(self, size: int, toppings: list[str]):
        super().__init__(size)
        self.toppings = toppings

    def get_toppings(self) -> list[str]:
        return self.toppings


def order_pizza(pizza: Pizza) -> None:
    print(f"Ordering a {pizza.get_size()}cm pizza with toppings: {', '.join(pizza.get_toppings())}")


def example() -> None:
    cheese_pizza = CheesePizza(12)
    order_pizza(cheese_pizza)

    pepperoni_pizza = PepperoniPizza(16)
    order_pizza(pepperoni_pizza)

    custom_pizza = CustomPizza(20, ["cheese", "pepperoni", "mushroom"])
    order_pizza(custom_pizza)


if __name__ == '__main__':
    example()
