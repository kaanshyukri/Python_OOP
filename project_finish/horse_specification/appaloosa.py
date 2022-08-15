from finish.horse_specification.horse import Horse


class Appaloosa(Horse):
    maximum_speed = 120
    increase_speed = 2

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @property
    def type(self):
        return Appaloosa.__name__
