def getdata():
    namelist = []
    surnamelist = []
    moredata = True
    while moredata :
        mylist=[]
        name=input("Enter Name ")
        while not name.isalpha():
            print("Name should be alphabet ")
            name = input("Enter Name")
        surname = input("Enter Surname ")
        while not surname.isalpha():
            print("Name should be alphabet ")
            surname = input("Enter Surname ")
        password = input("Enter Password ")
        age = int(input("Enter Age "))

        while not age not in range(12,50):
            print("Age should be 12-50 ")
            age = int(input("Enter age 12,50 "))
        username = input("Enter Username ")

    namelist.append(name)
    surnamelist.append(surname)
    more = input("More People Y/N ").lower()
    if more == "n":
            more = False

    if more == "N" or "n":
        moredata = False
        print("Names ", namelist)
        print("Surnames ", surnamelist)

getdata()
            
        
            
