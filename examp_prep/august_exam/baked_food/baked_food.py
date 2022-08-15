from abc import ABC, abstractmethod


class BakedFood(ABC):
    PORTION = 0

    @abstractmethod
    def __init__(self, name, price):
        self.name = name
        self.portion = self.PORTION
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty string or white space!")
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price cannot be less than or equal to zero!")
        self.__price = value

    def __repr__(self):
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
