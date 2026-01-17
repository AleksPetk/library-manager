
from datetime import datetime
from library_manager import LibraryManager, GeneralManager

#------------TODO: CONTROLS------------------------------------
def menu():
    list_menu = ["Add book", "Remove book", "List books", "Borrow book", "Return book", "General Manager Menu", "Exit"]
    print("\nLibrary Menu\n")
    for e, opt in enumerate(list_menu, 1):
        print(f"{e}. {opt}")
    return len(list_menu)

def get_user(min_v, max_v, name_tag):
    while True:
        try:
            user_get = int(input(f"{name_tag}: "))
            if min_v <= user_get <= max_v:
                return user_get
            else:
                print(f"{name_tag}s from {min_v} to {max_v}!")
        except ValueError:
            print("Numbers only!")

def fake_enter():
    fake = input("Press enter to continue: ")

#--------------------TODO: Menu Functions----------------

def add_book_main(manager_A):
    print("Our Books")
    manager_A.list_books()
    title = input("New Book Title: ").upper().strip()
    author = input("Author: ").capitalize().strip()
    year = get_user((datetime.now().year - 300), datetime.now().year, "Year")
    manager_A.add_book(title, author, year)
    fake_enter()

def remove_book_main(manager_A):
    print("What Book to Remove")
    manager_A.list_books()
    title_to_remove = input("Title name: ").upper().strip()
    manager_A.remove_book(title_to_remove)
    fake_enter()

def view_books_main(manager_A):
    print("\nAll Books\n")
    manager_A.list_books()
    fake_enter()

def borrow_books_main(manager_A):
    print("\nBorrow Book")
    manager_A.list_books()
    title_to_borrow = input("What book to borrow: ").upper().strip()
    manager_A.borrow_book(title_to_borrow)
    fake_enter()

def return_books_main(manager_A):
    print("\nReturn Book")
    manager_A.list_books()
    title_to_return = input("Title to return: ").upper().strip()
    manager_A.return_book(title_to_return)
    fake_enter()

def enter_general_menu(general_manager):
    while True:

        enter_allowed = general_manager.pass_check()

        if enter_allowed:
            general_manager_main(general_manager)
            print("General Manager Logged out!")
            break
        else:
            try_again = input("Do you want to try to enter again? Yes/No: ").lower().strip()
            if try_again == "yes":
                continue
            else: 
                break

def generate_txt_main(general_manager):
    print("Generate txt for today!")
    general_manager.generate_listtxt()
    print("Txt Generated!")
    fake_enter()



#----------------TODO: General Manager-------------------
def gen_menu():
    gen_Mlist = ["Add Many Books", "Remove All Books", "Generate List", "Exit"]
    print("\nGeneral Manager Menu\n")
    for e, opt in enumerate(gen_Mlist, 1):
        print(f"{e}. {opt}")
    return len(gen_Mlist)

def general_manager_main(general_manager):
    print("\nGeneral Manager\n")

    while True:
        gm_menu_len = gen_menu()
        user_choice = get_user(1, gm_menu_len, "Option")

        match user_choice:
            
            case 1: #Add Many Books
                add_many_books_gen(general_manager)
            case 2: #Remove All Books
                remove_all_books_gen(general_manager)
            case 3: #Generate List
                generate_txt_main(general_manager)
            case 4: #Back to main Menu
                print("Back to main menu")
                break


def add_many_books_gen(general_manager):
    print("\nAdd Many Books")
    print("Enter quantity number!")
    how_many = get_user(1, 30, "Number")
    general_manager.add_many_books(how_many)
    fake_enter()

def remove_all_books_gen(general_manager):
    print("\nDELETE ALL\n")
    delete_all_pass = input("Special Password: ")
    general_manager.remove_all_books(delete_all_pass)
    fake_enter()

#-------------------TODO: MAIN----------------------------

def main_loop():
    manager_A = LibraryManager()

    general_manager = GeneralManager()

    print("\nLIBRARY\n")

    while True:
        menu_len = menu()
        user_choice = get_user(1, menu_len, "Option")

        match user_choice:

            case 1: # Add Book
                add_book_main(manager_A)

            case 2: # Remove Book
                remove_book_main(manager_A)

            case 3: # List Books
                view_books_main(manager_A)

            case 4: # Borrow Book
                borrow_books_main(manager_A)

            case 5: # Return Book
                return_books_main(manager_A)
            
            case 6: # General Manager
                enter_general_menu(general_manager)

            case 7: # Exit Library
                print("Bye!")
                break


main_loop()