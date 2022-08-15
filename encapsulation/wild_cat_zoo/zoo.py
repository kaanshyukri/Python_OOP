from wild_cat_zoo.caretaker import Caretaker
from wild_cat_zoo.cheetah import Cheetah
from wild_cat_zoo.lion import Lion
from wild_cat_zoo.tiger import Tiger
from wild_cat_zoo.vet import Vet
from wild_cat_zoo.animal import Animal
from wild_cat_zoo.worker import Worker
from wild_cat_zoo.keeper import Keeper


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"
        if price > self.__budget:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        sum_of_workers_salary = sum(a.salary for a in self.workers)
        if self.__budget >= sum_of_workers_salary:
            self.__budget -= sum_of_workers_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_of_care_animals = sum(a.money_for_care for a in self.animals)
        if self.__budget >= sum_of_care_animals:
            self.__budget -= sum_of_care_animals
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        loins = [repr(a) for a in self.animals if isinstance(a, Lion)]
        result += f"----- {len(loins)} Lions:\n" + '\n'.join(loins)
        tigers = [repr(a) for a in self.animals if isinstance(a, Tiger)]
        result += "\n" + f"----- {len(tigers)} Tigers:\n" + '\n'.join(tigers)
        cheetah = [repr(a) for a in self.animals if isinstance(a, Cheetah)]
        result += "\n" + f"----- {len(cheetah)} Cheetahs:\n" + '\n'.join(cheetah)
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keeper = [repr(a) for a in self.workers if isinstance(a, Keeper)]
        result += f"----- {len(keeper)} Keepers:\n" + '\n'.join(keeper)
        caretaker = [repr(a) for a in self.workers if isinstance(a, Caretaker)]
        result += "\n" + f"----- {len(caretaker)} Caretakers:\n" + '\n'.join(caretaker)
        vet = [repr(a) for a in self.workers if isinstance(a, Vet)]
        result += "\n" + f"----- {len(vet)} Vets:\n" + '\n'.join(vet)
        return result

