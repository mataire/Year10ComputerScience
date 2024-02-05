def getdata():
    global descr, code, qty, cost, sp
  
    band = open("Bandq.txt", "a")
    more = True
    while more :
        array = []
        descr = input("Enter Description ")
        code = input("Enter Code ")
        qty = int(input("Enter Quantity "))
        cost = float(input("Enter Cost "))
        sp = input("Enter Selling Price ")
        array.append(descr)
        array.append(code)
        array.append(qty)
        array.append(cost)
        array.append(sp)
        array = map(str, array)
        line = (",").join(array)
        band.writelines(line + "\n")
        moreitems = input("More Items? ").lower()
        if moreitems == "n":
            more = False
        else:
            more = True

    band.close()
    
def readdata():
    band = open("Bandq.txt", "r")
    for line in band:
        fields = line.split(",")
        print ("Description  ", fields[0], "Code ", fields[1], "Quantity ", fields[2], "Cost ", fields[3], "Selling Price ", fields[4])
        value = cost * qty
        income = sp * qty
        print("Value ", value, "Income", income) 
    band.close()


def finddata():
    band = open("Bandq.txt", "r")
    name = input("Enter Item To Search ")
    found = False
    for line in band :
        fields = line.split(",")
        if name == fields[0]:
            print ("Item Found ")
            print ("Description  ", fields[0], "Code ", fields[1], "Quantity ", fields[2], "Cost ", fields[3], "Selling Price ", fields[4])
            import time
            time.sleep(5)
            found = True
            
    if not found:
        print("Item Not Found ")
    band.close()
    
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

getdata()
readdata()
finddata()