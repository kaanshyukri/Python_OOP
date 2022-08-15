from aqua_shop.controller import Controller

controller = Controller()

controller.add_aquarium("FreshwaterAquarium", "Name")
print(controller.report())