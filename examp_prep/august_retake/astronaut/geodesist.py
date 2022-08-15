from august_retake.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    oxygen_for_breathing = 10
    units_of_oxygen = 50

    def __init__(self, name):
        self.name = name
        self.oxygen = self.units_of_oxygen
        self.backpack = []