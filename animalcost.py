animal = ["cow", "sheep", "goat"]
values = [300, 120, 90]

def getdetails():
    global name, postcode, cows, sheep, goats
    
    name = input("Enter Name ")
    while not name.isalpha():
        print("Name Should Be Alphabetic ")
        name = input("Enter Name ")
    
    postcode = input("Enter Postcode ")
    cows = input("Enter Number Of Cows ")
    while not cows.isdigit():
        print("Number of cows should be a number ")
        cows = input("Enter Number Of Cows ")
    #casting
    
    cows = int(cows) #changing str to int
    
    sheep = input("Enter Number Of Sheep ")
    while not sheep.isdigit():
        print("Number of Sheep should be a number ")
        sheep = input("Enter Number Of Sheep ")
    #casting
    
    sheep = int(sheep) #changing str to int
    
    goats = input("Enter Number Of Goats ")
    while not goats.isdigit():
        print("Number of cows should be a number ")
        goats = input("Enter Number Of Goats ")
    #casting
    
    goats = int(goats) #changing str to int
    
def calculations():
    global total, cc, sc, gc
    
    cc = cows * values[0]
    sc = sheep * values[1]
    gc = goats * values[2]
    total = cc + sc + gc    

def printing():
    print("Name: ", name)
    print("Postcode: ", postcode)
    print("Cow Cost: ", cc )
    print("Sheep Cost: ", sc)
    print("Goat Cost: ", gc)
    print("Total: ", total)
    
getdetails()
calculations()
printing()