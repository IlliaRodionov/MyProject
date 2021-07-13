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
