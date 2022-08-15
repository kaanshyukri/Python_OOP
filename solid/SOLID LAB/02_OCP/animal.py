from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):

    def make_sound(self):
        return "woof-woof"


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Chicken(Animal):

    def make_sound(self):
        return "gli - gli"


def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog(), Cat(), Chicken()]
animal_sound(animals)
