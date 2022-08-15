from abc import ABC, abstractmethod

from examp_prep.apr import Owl


class Food(ABC):
    @abstractmethod
    def __init__(self, quantity):
        self.quantity = quantity


class Vegetable(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Fruit(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Meat(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Seed(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
