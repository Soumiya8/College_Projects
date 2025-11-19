confirmed_passengers = []
waiting_passengers = []
maximum_passengers = 5

def confirmed(name):
    if confirmed_passengers < len(maximum_passengers) :
        confirmed_passengers.append(name)
        
    else :
        waiting_passengers += name
    return 


