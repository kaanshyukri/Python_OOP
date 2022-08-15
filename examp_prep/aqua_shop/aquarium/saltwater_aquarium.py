from aqua_shop.aquarium.base_aquarium import BaseAquarium
from aqua_shop.fish.saltwater_fish import SaltwaterFish


class SaltwaterAquarium(BaseAquarium):

    def __init__(self, name):
        super().__init__(name, 25)

    @property
    def fish_type(self):
        return SaltwaterFish.__name__