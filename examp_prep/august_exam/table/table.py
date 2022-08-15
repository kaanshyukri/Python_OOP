from abc import ABC, abstractmethod

from august_exam.baked_food.baked_food import BakedFood
from august_exam.drink.drink import Drink


class Table(ABC):
    start_number = 0
    end_number = 0

    @abstractmethod
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if not self.start_number <= value <= self.end_number:
            if self.__class__.__name__ == "InsideTable":
                raise ValueError(f"Inside table's number must be between 1 and 50 inclusive!")
            else:
                raise ValueError(f"Outside table's number must be between 51 and 100 inclusive!")
        self.__table_number = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        return sum(f.price for f in self.food_orders) + sum(d.price for d in self.drink_orders)

    def clear(self):
        self.food_orders = []
        self.drink_orders = []
        self.is_reserved = False
        self.number_of_people = 0

    def free_table_info(self):
        if not self.is_reserved:

            return f"Table: {self.table_number}\n" \
                   f"Type: {self.__class__.__name__}\n" \
                   f"Capacity: {self.capacity}"


