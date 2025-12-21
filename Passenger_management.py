confirmed_passengers = []
waiting_list = []
maximum_passengers = 5

def confirmed():
    name = input("Enter the name to book ticket")
    if confirmed_passengers < len(maximum_passengers) :
        confirmed_passengers.append(name)
        print("Added to confirmed passenger list")

    else :
        waiting_list.append(name)
        print("Added to Waiting passenger list ")

def view_list():
    print("Passenger list is",confirmed_passengers)
    print("waiting list is",waiting_list)

def cancel_ticket():
    name = input("Enter the name to cancel")
    if name in confirmed_passengers:
        confirmed_passengers.remove(name)
        print(f"{name} removed from confirmed list")
    elif name in waiting_list:
        confirmed_passengers.append(waiting_list[0])
        waiting_list.remove(waiting_list[0])
        print("the modified waiting list is",waiting_list)
    else:
        print("The name is not found")

def menu():
    while True:
        print("1.Book ticket")
        print("2.View list")
        print("3.Cancel ticket")
        print("4.Exit")

        choice = int(input("Enter the choice"))
        if choice == 1 :
            confirmed() 
        elif choice  == 2 :
            view_list()
        elif choice == 3 :
            cancel_ticket()       
        elif choice == 4 :
            exit()
        else:
            print("Enter a valid choice")
menu()           


