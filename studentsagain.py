
#files reading and writing

def writetofile():
    students = open("Students.txt", "a")
    more = True
    while more :
        array = []
        name = input("Enter Name ")
        age = input("Enter Age ")
        hair = input("Enter Hair Colour ")
        array.append(name)
        array.append(age)
        array.append(hair)
        array = map(str, array)
        line = ",".join(array)
        students.writelines(line + "\n")
        morestudents = input("More Students ").lower()
        if morestudents == "n":
            more = False
            
    students.close()
    
#writetofile()
    
def readfile():
    students = open("Students.txt", "r")
    for line in students:
        fields = line.split(",")
        print ("name  ", fields[0], "age ", fields[1], "hair ", fields[2])
    students.close()
#readfile()
    
def findrec():
    students = open("Students.txt", "r")
    name = input("Enter Name To Search ")
    found = False
    for line in students :
        fields = line.split(",")
        if name == fields[0]:
            print ("Name Found ")
            print ("name  ", fields[0], "age ", fields[1], "hair ", fields[2])
            found = True
            
    if not found:
        print("Name Not Found ")
    students.close()
    
#findrec()
#Main Menu

choice = 0
while choice != 4 :
    print ("1 ... Enter Data ")
    print()
    print("2 ... Search For A Record ")
    print()
    print("3 ... Print All Records ")
    print()
    choice = int(input("Enter Choice "))
    if choice == 1:
        writetofile()
    elif choice == 2:
        readfile()
    elif choice == 3:
        findrec()