from august_exam.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    PORTION = 200

    def __init__(self, name, price):
        super().__init__(name, price)


