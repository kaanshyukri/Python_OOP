from august_retake.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        if planet not in self.planets:
            self.planets.append(planet)

    def remove(self, planet: Planet):
        if planet in self.planets:
            self.planets.pop(self.planets.index(planet))

    def find_by_name(self, name):
        for planet in self.planets:
            if planet.name == name:
                return planet

