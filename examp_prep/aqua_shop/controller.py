from aqua_shop.aquarium.freshwater_aquarium import FreshwaterAquarium
from aqua_shop.aquarium.saltwater_aquarium import SaltwaterAquarium
from aqua_shop.decoration.decoration_repository import DecorationRepository
from aqua_shop.decoration.ornament import Ornament
from aqua_shop.decoration.plant import Plant
from aqua_shop.fish.freshwater_fish import FreshwaterFish
from aqua_shop.fish.saltwater_fish import SaltwaterFish


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type != "FreshwaterAquarium" and aquarium_type != "SaltwaterAquarium":
            return "Invalid aquarium type."

        aquarium = None
        if aquarium_type == "FreshwaterAquarium":
            aquarium = FreshwaterAquarium(aquarium_name)
        else:
            aquarium = SaltwaterAquarium(aquarium_name)

        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        if decoration_type != "Ornament" and decoration_type != "Plant":
            return "Invalid decoration type."

        decoration = None
        if decoration_type == "Ornament":
            decoration = Ornament()
        else:
            decoration = Plant()

        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if decoration == "None":
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = self.find_aquarium_by_name(aquarium_name)
        if not aquarium:
            return

        self.decorations_repository.remove(decoration)
        aquarium.add_decoration(decoration)
        return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type != "FreshwaterFish" and fish_type != "SaltwaterFish":
            return f"There isn't a fish of type {fish_type}."

        aquarium = self.find_aquarium_by_name(aquarium_name)
        if not aquarium:
            return

        fish = None
        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
        else:
            fish = SaltwaterFish(fish_name, fish_species, price)

        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        aquarium.feed()
        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name):
        aquarium = self.find_aquarium_by_name(aquarium_name)
        value = sum(f.price for f in aquarium.fish) + sum(d.price for d in aquarium.decorations)
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = ""
        for aquarium in self.aquariums:
            result += str(aquarium) + "\n"

        return result.strip()

    def find_aquarium_by_name(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium
