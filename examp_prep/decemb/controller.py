from august_retake import MuscleCar
from august_retake import SportsCar
from august_retake import Driver
from august_retake import Race


class Controller:

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def find_driver(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver

    def find_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race

    def create_car(self, car_type, model, speed_limit):
        if car_type != "MuscleCar" and car_type != "SportsCar":
            return
        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")

        if car_type == "MuscleCar":
            new_car = MuscleCar(model, speed_limit)
        else:
            new_car = SportsCar(model, speed_limit)
        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name):
        driver = self.find_driver(driver_name)
        if driver:
            raise Exception(f"Driver {driver_name} is already created!")
        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name):
        race = self.find_race(race_name)
        if race:
            raise Exception(f"Race {race_name} is already created!")
        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name, car_type):
        driver = self.find_driver(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        for idx in range(len(self.cars) - 1, -1, -1):
            car = self.cars[idx]
            if car.__class__.__name__ == car_type:
                if not car.is_taken:
                    if driver.car is not None:
                        message = f"Driver {driver_name} changed his car from {driver.car.model} to {car.model}."
                        driver.car.is_taken = False
                        driver.car = car
                        driver.car.is_taken = True
                        return message
                    car.is_taken = True
                    driver.car = car
                    return f"Driver {driver_name} chose the car {driver.car.model}."
        raise Exception(f"Car {car_type} could not be found!")

    def add_driver_to_race(self, race_name, driver_name):
        race = self.find_race(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        driver = self.find_driver(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name):
        race = self.find_race(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        drivers = sorted(race.drivers, key=lambda x: -x.car.speed_limit)
        result = ''
        for idx in range(3):
            current_driver = drivers[idx]
            current_driver.number_of_wins += 1
            result += f"Driver {current_driver.name} wins the {race_name} race with a speed of" \
                      f" {current_driver.car.speed_limit}.\n"
        return result.strip()
