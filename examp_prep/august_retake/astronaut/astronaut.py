from abc import ABC, abstractmethod


class Astronaut(ABC):

    oxygen_for_breathing = 0
    units_of_oxygen = 0

    @abstractmethod
    def __init__(self, name):
        self.name = name
        self.oxygen = self.units_of_oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        if not value.strip():
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= self.oxygen_for_breathing

    def increase_oxygen(self, amount):
        self.oxygen += amount

    def __str__(self):
        result = f'Name: {self.name}' + '\n'
        result += f'Oxygen: {self.oxygen}' + '\n'
        result += f"Backpack items: {', '.join(self.backpack) if len(self.backpack) > 0 else 'none'}"

        return result
