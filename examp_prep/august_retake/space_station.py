from august_retake.astronaut.astronaut_repository import AstronautRepository
from august_retake.astronaut.biologist import Biologist
from august_retake.astronaut.geodesist import Geodesist
from august_retake.astronaut.meteorologist import Meteorologist
from august_retake.planet.planet import Planet
from august_retake.planet.planet_repository import PlanetRepository


class SpaceStation:
    completed = 0
    not_completed = 0
    in_space_astronaut = []

    def __init__(self):
        self.astronaut_repository = AstronautRepository()
        self.planet_repository = PlanetRepository()

    def add_astronaut(self, astronaut_type, name):

        if astronaut_type != "Biologist" and astronaut_type != "Geodesist" and astronaut_type != "Meteorologist":
            raise Exception("Astronaut type is not valid!")

        astronaut = self.astronaut_repository.find_by_name(name)

        if astronaut in self.astronaut_repository.astronauts:
            return f"{name} is already added."

        new_astronaut = None

        if astronaut_type == "Biologist":
            new_astronaut = Biologist(name)
        elif astronaut_type == "Geodesist":
            new_astronaut = Geodesist(name)
        elif astronaut_type == "Meteorologist":
            new_astronaut = Meteorologist(name)

        self.astronaut_repository.astronauts.append(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name, items):
        planet = self.planet_repository.find_by_name(name)

        if planet in self.planet_repository.planets:
            return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.items = items.split(", ")
        self.planet_repository.planets.append(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")
        current_astronauts = []
        sorted_astronauts = list(sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen))
        for astronaut_current in sorted_astronauts:
            if len(current_astronauts) < 5:
                if astronaut_current.oxygen > 30:
                    current_astronauts.append(astronaut_current)

        if not current_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")
        participated = 0

        for astronaut in current_astronauts:
            if not planet.items:
                break
            while astronaut.oxygen > 0 and planet.items:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            participated += 1

        if not planet.items:
            self.completed += 1
            return f"Planet: {planet_name} was explored. {participated} "\
                   f"astronauts participated in collecting items."
        else:
            self.not_completed += 1
            return "Mission is not completed."

    def report(self):
        result = f"{self.completed} successful missions!\n" \
                 f"{self.not_completed} missions were not completed!\n" \
                 f"Astronauts' info:\n"
        for astronaut in self.astronaut_repository.astronauts:
            result += f"Name: {astronaut.name}\n" \
                      f"Oxygen: {astronaut.oxygen}\n"
            result += f"Backpack items: {', '.join(astronaut.backpack) if len(astronaut.backpack) > 0 else 'none'}\n"

        return result.strip()


station = SpaceStation()
station.add_astronaut("Biologist", "Ivan")
station.add_astronaut("Geodesist", "Gosho")
station.add_astronaut("Meteorologist", "Ivo")
station.add_astronaut("Meteorologist", "Djaner")
station.add_astronaut("Biologist", "Kaan")
station.add_planet("Earth", "neshto, nishto, oshte_neshto")
station.send_on_mission("Earth")
print(station.report())