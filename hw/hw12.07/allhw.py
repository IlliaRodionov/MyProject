class Stadium:
    def __init__(self, name=None, opening_date=None, country=None, city=None, capacity=None):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city

    def presentation(self):
        return f"Stadium name: {self.name} \nWs opened: {self.opening_date} \nIn which country: {self.country} \n" \
               f"In what city: {self.city}"

    """the function counts the number of seats"""

    def capacity(self, left_side: int, right_side: int, central_part: int):
        number_of_places = left_side + right_side + central_part
        return number_of_places


May_Day_Stadium = Stadium(name="May Day Stadium", opening_date="1 mau 1989year", country="DPRK", city="Pyongyang")
print(May_Day_Stadium.presentation())
print(("Total capacity:"), May_Day_Stadium.capacity(left_side=75000, right_side=75000, central_part=150000))


# ==============================================================================================================


class Book:
    def __init__(self, name=None, year=None, genre=None, author=None, price=None):
        self.name = name
        self.year = year
        self.genre = genre
        self.author = author
        self.price = price

    def get_name(self):
        return f"Name: {self.name}\nYear of issue: {self.year}\nGengre: {self.genre}" \
               f"\nAuthor: {self.author}\nPrice:{self.price}"

    """function checks the rating"""

    def rating(self, book_rating: float, good_rating: float):
        if book_rating >= good_rating:
            print("Nice Rating:", book_rating)
        else:
            print("Low Rating:", book_rating)


Master_and_Margarita = Book(name="Master and Margarita", year="1929-1940", genre="Novel",
                            author="Michael Bulgakov", price="400$")

print(Master_and_Margarita.get_name())
(Master_and_Margarita.rating(book_rating=1.7, good_rating=2))


# ==============================================================================================================


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
