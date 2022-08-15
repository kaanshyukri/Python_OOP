from august_retake.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    oxygen_for_breathing = 5
    units_of_oxygen = 70

    def __init__(self, name):
        self.name = name
        self.oxygen = self.units_of_oxygen
        self.backpack = []
