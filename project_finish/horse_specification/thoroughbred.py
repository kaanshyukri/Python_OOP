from finish.horse_specification.horse import Horse


class Thoroughbred(Horse):
    maximum_speed = 140
    increase_speed = 3

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def type(self):
        return Thoroughbred.__name__

