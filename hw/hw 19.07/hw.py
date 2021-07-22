# Задание 1
# Создайте класс Device, который содержит информацию об устройстве.
# С помощью механизма наследования, реализуйте класс CoffeeMachine (содержит информацию о кофемашине),
# класс Blender (содержит информацию о блендере), класс MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые для работы методы.
class Divice:
    def __init__(self, name=None, production=None):
        self.name = name
        self.production = production

    def presentation(self):
        return f"Hello,my name {self.name}, Made in {self.production} "


class CoffeeMachine(Divice):
    def __init__(self, user_selection=None):
        super().__init__(user_selection)
        self.user_selection = user_selection

    def make_coffee(self):
        if user_selection == "black":
            print("Making black coffee")
        elif user_selection == "with milk":
            print("Making with milk")
        else:
            print("Select Coffee Type!!!")


class Blender(Divice):
    def __init__(self, ingredient=None):
        super().__init__()
        self.ingredient = ingredient

    #
    def make_fresh(self):
        print(f"Take {self.ingredient} beat.Your {self.ingredient}-fresh is ready")


class MeatGrinder(Divice):
    def __init__(self, meat=None):
        super().__init__()
        self.meat = meat

    def make_sloppy(self):
        print(f"Take {self.meat}.I’m ready to get started")


coffeemachine = Divice(name="CoffeeMachine", production="Germany")
print(coffeemachine.presentation())
user_selection = (input("What kind of coffee do you want :black and with milk? "))
coffeemachine = CoffeeMachine()
coffeemachine.make_coffee()

blender = Divice(name="Blender", production="Russia")
print(blender.presentation())
blender = Blender(ingredient="apple")
blender.make_fresh()

meatgrinder = Divice(name="MeatGrinder", production="Bulgari")
print(meatgrinder.presentation())
meatgrinder = MeatGrinder(meat="chicken meat")
meatgrinder.make_sloppy()


