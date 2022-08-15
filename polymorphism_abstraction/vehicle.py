from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    air_conditioner_consumption = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        total_consumption = (self.fuel_consumption + self.air_conditioner_consumption) * distance
        if total_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    air_conditioner_consumption = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance):
        total_consumption = (self.fuel_consumption + self.air_conditioner_consumption) * distance
        if total_consumption <= self.fuel_quantity:
            self.fuel_quantity -= total_consumption

    def refuel(self, fuel):
        refuel_hole = fuel * 0.95
        self.fuel_quantity += refuel_hole


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)





