from aqua_shop.fish.base_fish import BaseFish


# CAN LIVE ONLY IN Saltwateraquarium


class SaltwaterFish(BaseFish):
    INCREASE = 2

    def __init__(self, name, species, price):
        super().__init__(name, species, 5, price)
