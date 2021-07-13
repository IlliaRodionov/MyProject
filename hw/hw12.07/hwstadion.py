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
