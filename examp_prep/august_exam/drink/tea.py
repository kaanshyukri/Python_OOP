from august_exam.drink.drink import Drink


class Tea(Drink):
    PRICE = 2.5

    def __init__(self, name, portion, brand):
        super().__init__(name, portion, brand)
