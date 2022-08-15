from august_retake.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    oxygen_for_breathing = 15
    units_of_oxygen = 90

    def __init__(self, name):
        self.name = name
        self.oxygen = self.units_of_oxygen
        self.backpack = []
