from gym.customer import Customer
from gym.equipment import Equipment
from gym.exercise_plan import ExercisePlan
from gym.subscription import Subscription
from gym.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        self.__chek(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.__chek(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.__chek(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.__chek(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.__chek(subscription, self.subscriptions)

    def subscription_info(self, subscription_id):
        subscription = self.__find(subscription_id, self.subscriptions)
        customer = self.__find(subscription.customer_id, self.customers)
        trainer = self.__find(subscription.trainer_id, self.trainers)
        plan = self.__find(subscription.exercise_id, self.plans)
        equipment = self.__find(plan.equipment_id, self.equipment)

        return f"{repr(subscription)}\n" \
               f"{repr(customer)}\n" \
               f"{repr(trainer)}\n" \
               f"{repr(equipment)}\n" \
               f"{repr(plan)}"

    def __chek(self, entity, my_list):
        if entity not in my_list:
            my_list.append(entity)

    def __find(self, entity_id, my_list):
        for item in my_list:
            if item.id == entity_id:
                return item