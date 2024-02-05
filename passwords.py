datalist = []
passwordlist = []
inter = ['football', 'movies', 'music','rugby', 'cross country']

datafile = open("dataFile.txt ", "a")
passfile = open("passFile.txt ", "a")

more = True
while more:
    password = input("Enter password ")
    name = input("Enter Name ")
    age = int(input("Enter Age "))
    gender = input("Enter Gender ")
    add1 = input("Enter Address Line 1 ")
    add2 = input("Enter Address Line 2 ")
    add3 = input("Enter Address Line 3 ")
    postcode = input("Enter Postcode ")
    yourinterest = input("Enter Interest ").lower()
    while yourinterest not in inter:
        print("Incorrect Interest ")
        print("Correct Interests Are ", inter)
        yourinterest = input("Enter Intrest ")

    name = name.upper()
    username = name[0:4] + str(age)
    datalist.append(username)
    datalist.append(name)
    datalist.append(age)
    datalist.append(gender)
    datalist.append(add1)
    datalist.append(add2)
    datalist.append(add3)
    datalist.append(postcode)
    datalist.append(yourinterest)
    passwordlist.append(username)
    passwordlist.append(password)
    
    datalist = map(str, datalist)
    line = ",".join(datalist)
    datafile.writelines(line + "\n")
    
    passwordlist = map(str, passwordlist)
    line = ",".join(passwordlist)
    passfile.writelines(line + "\n")
    
    moredata = input("More Y/N ")
    counter = 0
    if moredata.upper() == "N":
        more = False
    
    datalist = []
    passwordlist = []
    
datafile.close()
passfile.close()
    
    