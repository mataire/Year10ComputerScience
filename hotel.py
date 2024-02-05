def acceptdetails():
    global name, destination, duration, accommodation, children
    name = input("Enter Name ")
    destination = input("Destination ")
    duration = int(input("Enter Duration "))
    accommodation = input("Enter Accommodation (Hotel Or Shared) ")
    children = int(input("Enter Ammount Of Children "))

def calculations():
    global hotelcost, childcost, durationcost, flightcost, charges

    if destination == "ct":
        flightcost = 1000
    else:
        flightcost = 800

    if children < 3 :
        childcost = 100
    else:
        childcost = children * 150


    if accommodation == "Hotel":
        hotelcost = 100
    else:
        hotelcost = 80

    if duration < 5 :
        durationcost = 200
    else:
        durationcost = 100

    charges = flightcost + childcost + hotelcost + durationcost

def printdetails():
    print("Name ", name)
    print("Destination ", destination)
    print("Duration ", duration)
    print("Accommodation ", accommodation)
    print("Children ", children)
    print("Flight cost: ", flightcost)
    print("Child Cost: ", childcost)
    print("Hotel Cost ", hotelcost)
    print("Duration Cost ", durationcost)
    print("Charges: ", charges)

acceptdetails()
calculations()
printdetails()
