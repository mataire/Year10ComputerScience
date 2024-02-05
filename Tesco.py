def getdata():
    global descr, code, qty, sp
  
    tesco = open("Tesco.txt", "a")
    more = True
    while more :
        array = []
        descr = input("Enter Description ")
        code = input("Enter Code ")
        qty = int(input("Enter Quantity "))
        sp = input("Enter Selling Price ")
        array.append(descr)
        array.append(code)
        array.append(qty)
        array.append(sp)
        array = map(str, array)
        line = (",").join(array)
        tesco.writelines(line + "\n")
        moreitems = input("More Items? ").lower()
        if moreitems == "n":
            more = False

    tesco.close()
#getdata()
    
def readdata():
    tesco = open("Tesco.txt", "r")
    for line in tesco:
        fields = line.split(",")
        print ("Description  ", fields[0], "Code ", fields[1], "Quantity ", fields[2], "Selling Price ", fields[3])
    tesco.close()
#readdata()


def finddata():
    tesco = open("Tesco.txt", "r")
    name = input("Enter Item To Search ")
    found = False
    for line in tesco :
        fields = line.split(",")
        if name == fields[0]:
            print ("Item Found ")
            print ("Description  ", fields[0], "Code ", fields[1], "Quantity ", fields[2], "Selling Price ", fields[3])
            found = True
            
    if not found:
        print("Item Not Found ")
    tesco.close()
    
#finddata()
#Main Menu

choice = 0
while choice != 4 :
    print ("1 ... Enter Data ")
    print()
    print("2 ... Read Data ")
    print()
    print("3 ... Find Data ")
    print()
    choice = int(input("Enter Choice "))
    if choice == 1:
        getdata()
    elif choice == 2:
        readdata()
    elif choice == 3:
        finddata()
