from august_retake.astronaut.astronaut import Astronaut


class AstronautRepository:

    def __init__(self):
        self.astronauts = []

    def add(self, astronaut: Astronaut):
        if astronaut not in self.astronauts:
            self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        if astronaut in self.astronauts:
            self.astronauts.pop(self.astronauts.index(astronaut))

    def find_by_name(self, name):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut

    def find_astronauts_for_mission(self):
        result = sorted([x for x in self.astronauts if x.oxygen > 30], key=lambda x: -x.oxygen)[0:5]
        return result
