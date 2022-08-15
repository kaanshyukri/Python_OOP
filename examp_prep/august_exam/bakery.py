from august_exam.baked_food.bread import Bread
from august_exam.baked_food.cake import Cake
from august_exam.drink.tea import Tea
from august_exam.drink.water import Water
from august_exam.table.inside_table import InsideTable
from august_exam.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty string or white space!")
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def find_name(self, new_list, repository):
        for item in repository:
            if item.name == new_list.name:
                return item

    def find_table_number(self, number, repository):
        for item in repository:
            if item.table_number == number:
                return item

    def add_food(self, food_type, name, price):
        if food_type == "Bread" or food_type == "Cake":
            new_food = None
            if food_type == "Bread":
                new_food = Bread(name, price)
            elif food_type == "Cake":
                new_food = Cake(name, price)

            if self.find_name(new_food, self.food_menu):
                raise Exception(f"{food_type} {name} is already in the menu!")

            self.food_menu.append(new_food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type, name, portion, brand):
        if drink_type == "Tea" or drink_type == "Water":

            new_drink = None
            if drink_type == "Tea":
                new_drink = Tea(name, portion, brand)
            elif drink_type == "Water":
                new_drink = Water(name, portion, brand)

            if self.find_name(new_drink, self.drinks_menu):
                raise Exception(f"{drink_type} {name} is already in the menu!")

            self.drinks_menu.append(new_drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type, table_number, capacity):
        if table_type == "InsideTable" or table_type == "OutsideTable":

            new_table = None
            if table_type == "InsideTable":
                new_table = InsideTable(table_number, capacity)
            else:
                new_table = OutsideTable(table_number, capacity)

            if self.find_table_number(table_number, self.tables_repository):
                raise Exception(f"Table {table_number} is already in the bakery!")
            self.tables_repository.append(new_table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number, *food_names):
        table = self.find_table_number(table_number, self.tables_repository)

        if not table:
            return f"Could not find table {table_number}"
        ordered = []
        not_ordered = []
        for food_name in food_names:
            for food in self.food_menu:
                if food.name == food_name:
                    table.order_food(food)
                    ordered.append(food_name)

        for food_name in food_names:
            if food_name not in ordered:
                not_ordered.append(food_name)

        result = f"Table {table.table_number} ordered:" + "\n"
        for ordered_food in table.food_orders:
            result += str(ordered_food) + "\n"
        result += f"{self.name} does not have in the menu:\n"
        for food_not_in_the_menu in not_ordered:
            result += f"{food_not_in_the_menu}\n"

        return result.strip()

    def order_drink(self, table_number, *drink_names):
        table = self.find_table_number(table_number, self.tables_repository)

        if not table:
            return f"Could not find table {table_number}"
        ordered = []
        not_ordered = []
        for drink_name in drink_names:
            for drink in self.drinks_menu:
                if drink.name == drink_name:
                    table.order_drink(drink)
                    ordered.append(drink_name)

        for drink_name in drink_names:
            if drink_name not in ordered:
                not_ordered.append(drink_name)

        result = f"Table {table.table_number} ordered:" + "\n"
        for ordered_drink in table.drink_orders:
            result += str(ordered_drink) + "\n"
        result += f"{self.name} does not have in the menu:\n"
        for food_not_in_the_menu in not_ordered:
            result += f"{food_not_in_the_menu}\n"

        return result.strip()

    def leave_table(self, table_number):
        table = self.find_table_number(table_number, self.tables_repository)
        bill = table.get_bill()
        self.total_income += bill
        table.clear()

        return f"Table: {table_number}\n" \
               f"Bill: {bill:.2f}"

    def get_free_tables_info(self):
        result = ""
        for table in self.tables_repository:
            if not table.is_reserved:
                result += table.free_table_info() + "\n"
        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"





