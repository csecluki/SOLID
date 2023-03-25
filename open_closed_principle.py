"""
The Open/Closed Principle (OCP) is an essential design principle in object-oriented programming that emphasizes the need for software entities,
such as classes, modules, and functions, to be open for extension but closed for modification. In simpler terms, once a software entity has been
designed and tested, it should not be changed to add new features or modify existing behavior. Instead, it should be created in a way that
enables new functionality to be added through extension or modification of its existing behavior.

To achieve the Open/Closed Principle, developers often rely on abstractions, interfaces, and inheritance. By using abstractions and interfaces
that define the behavior of a software entity, and by leveraging inheritance to implement that behavior, they can create classes and modules
that are open for extension (by allowing new behavior to be added through the creation of new subclasses) but closed for modification (by avoiding
changes to the existing classes or modules).

By adhering to the Open/Closed Principle, software can be designed to be more modular, maintainable, and reusable. This approach also simplifies
the process of adding new features and functionality without risking the introduction of bugs or causing issues with existing functionality.
"""


import abc
from abc import ABC, abstractmethod


class Pizza(ABC):

    @abstractmethod
    def get_price(self) -> float:
        pass


class Margherita(Pizza):

    def get_price(self) -> float:
        return 12.0


class Pepperoni(Pizza):

    def get_price(self) -> float:
        return 15.0


class PizzaOrder:

    def __init__(self, pizzas, online_order: bool = False):
        self.pizzas = pizzas
        self.online_order = online_order

    def get_total_price(self) -> float:
        return sum(pizza.get_price() for pizza in self.pizzas)


class Discount(abc.ABC):

    @abstractmethod
    def apply_discount(self, pizza_order: PizzaOrder) -> float:
        pass


class LargeOrderDiscount(Discount):

    def apply_discount(self, pizza_order: PizzaOrder) -> float:
        if len(pizza_order.pizzas) >= 4:
            return pizza_order.get_total_price() * 0.1
        else:
            return 0.0


class OnlineOrderDiscount(Discount):

    def apply_discount(self, pizza_order: PizzaOrder) -> float:
        if pizza_order.online_order:
            return pizza_order.get_total_price() * 0.04
        return 0.0


def example() -> None:
    order1 = PizzaOrder([Margherita(), Pepperoni(), Margherita()], online_order=True)
    order2 = PizzaOrder([Margherita(), Margherita(), Margherita(), Margherita(), Margherita()])

    discounts = [LargeOrderDiscount(), OnlineOrderDiscount()]

    order1_total = order1.get_total_price() - sum(discount.apply_discount(order1) for discount in discounts)
    order2_total = order2.get_total_price() - sum(discount.apply_discount(order2) for discount in discounts)

    print(f"Order 1 total: ${order1_total}")
    print(f"Order 2 total: ${order2_total}")


if __name__ == '__main__':
    example()
