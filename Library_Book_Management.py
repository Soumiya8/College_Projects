#Lib_book management
library = {}
def add_book():
    book_id = input("Book ID")
    library[book_id] = {
        "title" : input("Title"),
        "author" : input("Author"),
        "status" : "Available",
        "section" : input("section")
    }

def update_status():
    book_id = input("book Id")
    library[book_id]["status"] = input ("new status")


def transfer_section():
    book_id = input("Enter the id")
    library[book_id]["section"] = input("New section")

def display_books():
    for b in library():
        print(b)

while True:
    print("\nLibrary Management System")
    print("1.Add book")
    print("2.Update status")
    print("3.Transfer selection")
    print("4.Display books")
    print("5.Exit")

    choice = int(input("Enter the choice(1/2/3/4/5)"))

    if choice == 1:
        add_book()
    elif choice == 2:
        update_status()
    elif choice == 3:
        transfer_section()
    elif choice == 4:
        display_books()
    elif choice == 5:
        break
    else:
        print("Enter the valid choice")
