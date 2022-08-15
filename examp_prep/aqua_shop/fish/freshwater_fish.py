from aqua_shop.fish.base_fish import BaseFish


#CAN LIVE ONLY IN FRESHWATERAQUARIUM


class FreshwaterFish(BaseFish):
    INCREASE = 3

    def __init__(self, name, species, price):
        super().__init__(name, species, 3, price)
