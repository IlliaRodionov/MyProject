class Stadium:
    def __init__(self, name, opening_date, country, city, central_part,
                 left_side, right_side):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.left_side = left_side
        self.right_side = right_side
        self.central_part = central_part

    def presentation(self):
        return f"Stadium name: {self.name} \nWs opened: {self.opening_date} \nIn which country: {self.country} \n" \
               f"In what city: {self.city}"

    """the method counts the number of seats"""

    def capacity(self):
        return f"central_part {self.central_part}, right_side{self.right_side}," \
               f"left_side {self.left_side}"


may_day_stadium = Stadium(name="May Day Stadium", opening_date="1 mau 1989year", country="DPRK", city="Pyongyang",
                          left_side=150000, right_side=150000, central_part=300000)
print(may_day_stadium.presentation())
print(("Total capacity:"), may_day_stadium.capacity())
