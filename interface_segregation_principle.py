"""
The Interface Segregation Principle (ISP) is an object-oriented design principle that suggests creating interfaces that cater to the
specific needs of the clients that use them. The principle emphasizes that clients should not be compelled to depend on interfaces
that offer methods they do not use.

Breaking down large and general-purpose interfaces into smaller and more focused ones can accomplish the Interface Segregation Principle.
Each interface should meet the requirements of a specific client, which can also be achieved using abstract classes. Abstract classes
provide a default implementation for some methods, while others remain abstract for subclasses to implement only the necessary methods.

Following the Interface Segregation Principle makes the code more flexible and adaptable to changes. It reduces coupling between classes,
aids code reuse and increases testability. As clients only interact with methods relevant to their needs, it helps reduce the risk of
errors and bugs, making code more maintainable and understandable.
"""

from abc import ABC, abstractmethod


class Topping(ABC):

    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


class CheeseTopping(Topping):

    def __init__(self):
        self.description = "Cheese"
        self.price = 1.20

    def get_price(self) -> float:
        return self.price

    def get_description(self) -> str:
        return self.description


class PepperoniTopping(Topping):

    def __init__(self):
        self.description = "Pepperoni"
        self.price = 1.50

    def get_price(self) -> float:
        return self.price

    def get_description(self) -> str:
        return self.description


class MushroomTopping(Topping):

    def __init__(self):
        self.description = "Mushroom"
        self.price = 0.99

    def get_price(self) -> float:
        return self.price

    def get_description(self) -> str:
        return self.description


class Pizza(ABC):

    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def add_topping(self, topping: Topping) -> None:
        pass

    @abstractmethod
    def get_description(self) -> str:
        pass


class CheesePizza(Pizza):

    def __init__(self):
        self.description = "Cheese Pizza"
        self.price = 8.99
        self.toppings = [CheeseTopping()]

    def get_price(self) -> float:
        return self.price + sum(topping.get_price() for topping in self.toppings)

    def add_topping(self, topping: Topping) -> None:
        self.toppings.append(topping)

    def get_description(self) -> str:
        return self.description


class Order:

    def __init__(self):
        self.pizzas = []

    def add_pizza(self, pizza) -> None:
        self.pizzas.append(pizza)

    def get_total_price(self) -> float:
        return sum(pizza.get_price() for pizza in self.pizzas)

    def print_order(self) -> None:
        for pizza in self.pizzas:
            print(pizza.get_description())


def example():
    order = Order()
    cheese_pizza = CheesePizza()
    cheese_pizza.add_topping(PepperoniTopping())
    cheese_pizza.add_topping(MushroomTopping())
    order.add_pizza(cheese_pizza)

    print(f"Order total: ${order.get_total_price()}")
    print("Order contents:", end=" ")
    order.print_order()


if __name__ == '__main__':
    example()
