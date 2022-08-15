from finish.horse_race import HorseRace
from finish.horse_specification.appaloosa import Appaloosa
from finish.horse_specification.thoroughbred import Thoroughbred
from finish.jockey import Jockey


class HorseRaceApp:

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type, horse_name, horse_speed):
        if horse_type != "Appaloosa" and horse_type != "Thoroughbred":
            return

        if self.find_horse_by_name(horse_name):
            raise Exception(f"Horse {horse_name} has been already added!")

        new_horse = None
        if horse_type == "Appaloosa":
            new_horse = Appaloosa(horse_name, horse_speed)
        else:
            new_horse = Thoroughbred(horse_name, horse_speed)

        self.horses.append(new_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name, age):

        if self.find_jockey_by_name(jockey_name):
            raise Exception(f"Jockey {jockey_name} has been already added!")

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type):

        if self.find_race_by_type(race_type):
            raise Exception(f"Race {race_type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name, horse_type):

        jockey = self.find_jockey_by_name(jockey_name)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        horse = self.find_horse_by_type_last_added(horse_type)

        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if horse and jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type, jockey_name):
        race = self.find_race_by_type(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self.find_jockey_by_name(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type):
        race = self.find_race_by_type(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        fastest = None

        for jockey in race.jockeys:
            if fastest is not None:
                if jockey.horse.speed > fastest.horse.speed:
                    fastest = jockey
            else:
                fastest = jockey

        return f"The winner of the {race_type} race, with a speed of {fastest.horse.speed}km/h is {fastest.name}!" \
               f" Winner's horse: {fastest.horse.name}."

    def find_horse_by_name(self, horse_name):
        for horse in self.horses:
            if horse.name == horse_name:
                return horse

    def find_jockey_by_name(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey

    def find_race_by_type(self, race_type):
        for race in self.horse_races:
            if race.race_type == race_type:
                return race

    def find_horse_by_type_last_added(self, horse_type):
        for idx in range(len(self.horses) - 1, -1, -1):
            current = self.horses[idx]
            if current.type == horse_type:
                if not current.is_taken:
                    return current


