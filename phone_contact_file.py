#phone contacts file handling
def add_contact():
    name = input("enter the name: ")
    phone = input("enter the phone number: ")
    with open("contact.txt","a") as f:
        f.write(name + "-" + phone + "\n")

def view_contacts():
    try:
        with open("contact.txt","r") as f:
            print(f.read())
    except:
        print("File not Found")

def search_contact():
    name = input("Enter the name")
    try:
        with open("contact.txt","r") as f:
            for line in f:
                if line.startswith(name):
                    print(line)
    except:
        print("File error")

while True:
    print("\nPhone Book")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.") 
