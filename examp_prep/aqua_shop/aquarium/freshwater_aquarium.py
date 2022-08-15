from aqua_shop.aquarium.base_aquarium import BaseAquarium
from aqua_shop.fish.freshwater_fish import FreshwaterFish


class FreshwaterAquarium(BaseAquarium):

    def __init__(self, name):
        super().__init__(name, 50)

    @property
    def fish_type(self):
        return FreshwaterFish.__name__