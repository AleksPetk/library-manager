
from datetime import datetime
import json
from book import Book
import random, os




class LibraryManager:
    """
    Controls the library system:
    - owns all books
    - owns file persistence
    - applies rules
    """
    books = {} # ONE source of truth: title -> Book

    def __init__(self, filename = "library.json"):
        self.filename = filename
        self.load()

    def load(self):
        """
        Load books from JSON.
        If file is missing or corrupted, start empty.
        """
        try:
            with open(self.filename, "r") as f:
                raw = json.load(f)

            LibraryManager.books.clear()
            for title, data in raw.items():
                LibraryManager.books[title] = Book.from_dict(data)

        except (FileNotFoundError, json.JSONDecodeError):
            LibraryManager.books.clear()

    def save(self):
        """
        Save all books to JSON.
        """
        data = {title: book.to_dict() for title, book in LibraryManager.books.items()}
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)
        print("Saved")

    def add_book(self, title, author, year):
        if title in LibraryManager.books:
            print("Book already exists.")
            return False
        LibraryManager.books[title] = Book(title, author, year)
        print(f"{title} added!")
        self.save()
        return True

    def remove_book(self, title):
        if title not in LibraryManager.books:
            print("Book not found.")
            return
        else: 
            print(f"{LibraryManager.books[title]}")
            conf = input("Do you really want to remove? Yes/No: ").strip().lower()
            if conf == "yes":
                del LibraryManager.books[title]
                print(f"{title} Removed!")
                self.save()
            else:
                print("Remove proccess canceled!")

    def list_books(self):
        if not LibraryManager.books:
            print("Library empty.")
        for book in LibraryManager.books.values():
            print(book)

    def borrow_book(self, title):
        if title not in LibraryManager.books:
            print("Book not found.")
            return

        book = LibraryManager.books[title]
        if not book.available:
            print("Book already borrowed.")
            return

        book.borrow()
        print("Book borrowed.")
        self.save()
        

    def return_book(self, title):
        if title not in LibraryManager.books:
            print("Book not found.")
            return

        book = LibraryManager.books[title]
        if book.available:
            print("Book is not borrowed.")
            return

        book.return_book()
        print("Book returned.")
        self.save()
        


class GeneralManager(LibraryManager):

    def __init__(self, filename="library.json"):
        self.password = "Aleks9"
        self.attempts = 3
        self.recovery = "AleksAleks9"
        self.access = True
        super().__init__(filename)

    def pass_check(self):

        if self.access == False:
            print("Access Blocked!")
            check_recovery = input("Enter recovery pass: ")
            if self.recovery == check_recovery:
                self.access = True
                print("Access Unblocked!")
            else:
                print("Wrong recovery password!")
                print("Access stays blocked!")
            return False

        else:
            print(f"You have {self.attempts} attempts")
            input_pass = input("General Manager Password: ")
        
            if self.password == input_pass:
                self.attempts = 3
                return True
            else:
                print("Wrong password!")
                self.attempts -= 1
                
                if self.attempts <= 0:
                    print("Access Blocked!")
                    self.access = False
                    self.attempts = 3
                    return False
                else:
                    return False
        


    def add_many_books(self, how_many):
        book_names_list = ["Sels Journey", "Lord of Sels", "Cry money", "Panda Back", "Sleeping Cats",
                           "Crazy Song", "Nami up", "Swimming Dogs", "Monkey Bite", "Snack Time"]
        book_parts_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        book_authors_name = ["Aleks", "Nami", "Mai", "Nikita",  "Pavel", "Sonya", "Riku", "Tonko",
                             "Clara", "Shipu", "Mazuhiro", "Dagobara", "Namadara", "Putyo"]
        year_now = datetime.now().year
        year_end = year_now - 150
        not_addet = []

        for i in range(how_many):
            name1 = random.choice(book_names_list).upper().strip()
            name2 = random.choice(book_parts_list).upper().strip()
            title = f"{name1} {name2}"
            author = random.choice(book_authors_name)
            year = random.randint(year_end, year_now)
            added_or = self.add_book(title, author, year)
            if added_or == False:
                not_addet.append(title)
        if not_addet:
            for e, titl in enumerate(not_addet, 1):
                print(f"{e}. {titl} Not Added! Already exist!")
            print(f"{len(not_addet)} from {how_many} book/s was not Added!")

    def remove_all_books(self, delete_all_pass):

        special_password = "DeleteAll"

        if special_password == delete_all_pass:
            conf_code = random.randint(10000, 99999)
            print(f"Enter Code: | {conf_code} | to DELETE ALL BOOKS")
            code_u = input("Code: ").strip()
            if not code_u.isdigit():
                print("Something Wrong:")
            else:
                code_u = int(code_u)
                if code_u == conf_code:
                    self.list_books()
                    LibraryManager.books.clear()
                    print("All Books Removed!")
                    self.save()
                
        else:
            print("Wrong Password! Bye!")


    def generate_listtxt(self):
        txt_folder = "txtFolder"

        if not os.path.exists(txt_folder):
            os.mkdir(txt_folder)

        txt_file = f"text_file_{datetime.now().strftime('%Y-%m-%d')}.txt"
        txt_path = os.path.join(txt_folder, txt_file)

        

        with open(txt_path, "w") as f:
            for e, (key, value) in enumerate(LibraryManager.books.items(), 1):
                text_is = f"{e}. {key} - {value}"
                f.write(f"{text_is}\n")
        
        
            



        


