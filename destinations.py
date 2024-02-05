dest = ["ny", "du", "hr"]
flights = [600, 400, 800]
hotelcost = [120, 90, 80]

def getdetails():
    global name, kids, destination, adults
    
    destination = input("Enter Destination ").lower()
    name = input("Enter Name ")
    while not name.isalpha():
        print("Name Should Be Alphabetic ")
        name = input("Enter Name ")
    
    kids = input("Enter Number Of Kids ")
    while not kids.isdigit() or int(kids) > 3:
        print("Kids should be less than 3 ")
        kids = input("Enter Number Of Kids ")
    #casting
    kids = int(kids) #changing str to int
    
    adults = input("Enter Number Of Adults ")
    while not adults.isdigit() or int(adults) > 3:
        print("Adults should be a number and over the age of 3 ")
        adults = input("Enter Number Of Adults ")
    #casting
    adults = int(adults) #changing str to int
    
def calculations():
    global total, ktf, khc, atf, ahc, kt, at
    
    if destination == dest[0]:
        ktf = flights[0] * 50/100
        khc = hotelcost[0] * 80/100
        atf = adults * flights[0]
        ahc = hotelcost[0] * adults
        total = atf + ahc + ktf * kids + khc * kids
    
    elif destination == dest[1]:
        ktf = flights[1] * 50/100
        khc = hotelcost[1] * 80/100
        atf = adults * flights[1]
        ahc = hotelcost[1] * adults
        total = atf + ahc + ktf * kids + khc * kids
    
    else:
        ktf = flights[2] * 50/100
        khc = hotelcost[2] * 80/100
        atf = adults * flights[2]
        ahc = hotelcost[2] * adults
        total = atf + ahc + ktf * kids + khc * kids

def printing():
    print("Name ", name)
    print("Destination ", destination)
    print("Kids Fare ", ktf )
    print("Kids Hotel Cost ", khc)
    print("Adults Fare", atf)
    print("Adults Hotel Cost", ahc)
    print("Total ", total)
    
getdetails()
calculations()
printing()
    
    
    
        
    
