from examp_prep.apr import Mammal


class Mouse(Mammal):
    @property
    def allowed_food(self):
        return ["Vegetables", "Fruits"]

    @property
    def weight_incremental(self):
        return 0.10

    def make_sound(self):
        return "Squeak"


class Cat(Mammal):
    @property
    def allowed_food(self):
        return ["Vegetables", "Meat"]

    @property
    def weight_incremental(self):
        return 0.30

    def make_sound(self):
        return "Meow"


class Dog(Mammal):
    @property
    def allowed_food(self):
        return ["Meat"]

    @property
    def weight_incremental(self):
        return 0.40

    def make_sound(self):
        return "Woof!"


class Tiger(Mammal):
    @property
    def allowed_food(self):
        return ["Meat"]

    @property
    def weight_incremental(self):
        return 1.00

    def make_sound(self):
        return "ROAR!!!"

