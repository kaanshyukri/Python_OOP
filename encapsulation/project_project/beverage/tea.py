from project_project.beverage.hot_beverage import HotBeverage


class Tea(HotBeverage):
    def __init__(self, name, price, millilitres):
        super().__init__(name, price, millilitres)
