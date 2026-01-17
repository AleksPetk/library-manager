class Book:
    """
    Represents ONE book.
    This class should NOT know about files or menus.
    """

    def __init__(self, title, author, year, available=True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available

    def borrow(self):
        # Borrowing means the book is no longer available
        self.available = False

    def return_book(self):
        # Returning restores availability
        self.available = True

    def to_dict(self):
        """
        Convert Book object to dictionary.
        Needed for JSON saving.
        """
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "available": self.available
        }

    @staticmethod
    def from_dict(data):
        """
        Create a Book object from dictionary (JSON load).
        """
        return Book(
            data["title"],
            data["author"],
            data["year"],
            data["available"]
        )

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} | {self.author} | {self.year} | {status}"