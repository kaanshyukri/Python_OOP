from abc import abstractmethod, ABC
import time


class Workable(ABC):

    @abstractmethod
    def work(self):
        pass


class Eateble(ABC):

    @abstractmethod
    def eat(self):
        pass


class Worker(Workable, Eateble):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(Workable, Eateble):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(Workable):

    def work(self):
        print("I'm a robot. I'm working....")



class Manager(ABC):
    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class Work(Manager):


    def set_worker(self, worker):
        assert isinstance(worker, Workable), "`worker` must be of type {}".format(Workable)

        self.worker = worker

    def manage(self):
        self.worker.work()


class Eat(Manager):


    def set_worker(self, worker):
        assert isinstance(worker, Eateble), "`worker` must be of type {}".format(Eateble)

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


work_manager = Work()
break_manager = Eat()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass

