from abc import ABC, abstractmethod


class BaseAquarium(ABC):

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    @property
    @abstractmethod
    def fish_type(self):
        pass

    def calculate_comfort(self):
        return sum(x.comfort for x in self.decorations)

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return 'Not enough capacity.'
        if self.fish_type != fish.__class__.__name__:
            return 'Water not suitable.'
        self.fish.append(fish)
        return f'Successfully added {fish.__class__.__name__} to {self.name}.'

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        return f"{self.name}:\n" \
               f"Fish: {' '.join(x.name for x in self.fish) if self.fish else 'none'}\n" \
               f"Decorations: {len(self.decorations)}\n" \
               f"Comfort: {self.calculate_comfort()}"



