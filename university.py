def getdata():
    global name, points, gender, age
    more = True
    while more:
        name = input("Enter Name ")
        points = int(input("Enter Points "))
        gender = input("Enter Gender ")
        age = int(input("Enter Age "))
        moreinputs = input("More Inputs? (y/n) ")
        if moreinputs == "y":
            more = True
        else:
            more = False

#End Of Input

def allocate():
    global uni

    if points == 16 and age == 18 :
        if gender == "f":
            uni = "Bedfordshire Univeristy "
        else :
            uni = "Cambridge University "

    elif points < 16 and age == 20 :
        if gender == "f":
            uni = "Northampton University "
        else:
            uni = "Birmingham University "
    else:
        uni = "Reading University "

    print("Name ", name , "Uni ", uni) 
    university = open("University", "a")
    array = []
    array.append(name)
    array.append(points)
    array.append(gender)
    array.append(age)
    array.append(uni)

    array = map(str, array)
    line = ",".join(array)
    university.writelines(line + "\n")
    university.close()

more = False
while more:
    getdata()
    allocate()
    morestud = input("More Students Y/N ").lower()
    if morestud == "n":
        more = False

def readdata():
    university = open("University", "r")
    for line in university :
        fields = line.split(",")
        print("Name ", fields[0], "Uni ", fields[0])
    university.close()


getdata()
allocate()
readdata()
