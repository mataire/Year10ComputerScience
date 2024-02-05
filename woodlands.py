def getdata():
    global animalsp, age, colour, habitat
  
    woodlands = open("Animals.txt", "a")
    more = True
    while more :
        array = []
        #colourlist = ["Brown", "Black", "Silver"]
        
        animalsp = input("Enter Animal ")
        age = int(input("Enter Age "))
        colourlist = ["Black", "Brown", "Silver"]
        colour = input("Enter Colour ").lower()
        while colour not in colourlist :
            print("Colour Should Be ", colourlist)
            colour = input("Enter Habitat ").lower()
        habitatlist = ["water", "land"]
        habitat = input("Enter Habitat ").lower()
        while habitat not in habitatlist :
            print("Habitat Should Be ", habitatlist)
            habitat = input("Enter Habitat ").lower()
        array.append(animalsp)
        array.append(age)
        array.append(colour)
        array.append(habitat)
        array = map(str, array)
        line = (",").join(array)
        woodlands.writelines(line + "\n")
        moreitems = input("More Items? ").lower()
        if moreitems == "n":
            more = False

    woodlands.close()
#getdata()
    
def readdata():
    woodlands = open("Animals.txt", "r")
    for line in woodlands:
        fields = line.split(",")
        print ("Animal  ", fields[0], "Age ", fields[1], "Colour ", fields[2], "Habitat ", fields[3])
    woodlands.close()
#readdata()


def finddata():
    woodlands = open("Animals.txt", "r")
    name = input("Enter Item To Search ")
    found = False
    for line in woodlands :
        fields = line.split(",")
        if name == fields[0]:
            print ("Item Found ")
            print ("Animal  ", fields[0], "Age ", fields[1], "Colour ", fields[2], "Habitat ", fields[3])
            found = True
            
    if not found:
        print("Item Not Found ")
    woodlands.close()
    
#finddata()
#Main Menu

choice = 0
while choice != 4 :
    print ("1 ... Enter Animal Data ")
    print()
    print("2 ... Read Current Animal Data ")
    print()
    print("3 ... Search For An Animal ")
    print()
    choice = int(input("Enter Choice "))
    if choice == 1:
        getdata()
    elif choice == 2:
        readdata()
    elif choice == 3:
        finddata()