class Car:
    def __init__(self, name=None, year_of_issue=None, manufacturer=None, engine=None, color=None, price=None,
                 transmission=None):
        self.name = name
        self.year_of_issue = year_of_issue
        self.manufacturer = manufacturer
        self.engine = engine
        self.color = color
        self.price = price
        self.transmission = transmission

    def get_name(self):
        return f"This car {self.name}, Production {self.year_of_issue}, " \
               f"Made in {self.manufacturer}."

    def exclusive_options(self):
        return f"Unique engine {self.engine},\n{self.transmission},\nIn the most unusual color{self.color}"

    """" The function determines the final cost"""

    def get_price(self, price: int, color_price: int, transmission_price: int):
        final_price = price + color_price + transmission_price
        currency = "$"
        return str(final_price) + currency


bmw = Car(name="BMW", year_of_issue=2012, manufacturer="Germany", engine=":2.0(diesel)", color=":Electron Blue Pearl",
          transmission="8-speed automatic transmission", price="12000$")
print(bmw.get_name())
print(bmw.exclusive_options())
print(bmw.get_price(12000, 500, 2500, ))

opel = Car(name="Opel", year_of_issue=2021, manufacturer="France", engine=":3.3(petrol)", color=":Orange Lava",
           transmission="6-Manual Transmission", price="45000$")
print(opel.get_name())
print(opel.exclusive_options())
print(("Final price:"), opel.get_price(45000, 950, 1200))
