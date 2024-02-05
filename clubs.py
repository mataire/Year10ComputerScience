def getdetails():
    global firstname, age, SATS, gender, transport

    firstname = input("Enter First Name ")
    age = int(input("Enter Age "))
    SATS = int(input("Enter SATS "))
    transport = input("Enter Transport ")
    
    genderlist = ["m", "f"]
    gender = input("Enter Gender ").lower()
    while gender not in genderlist :
        print("Gender Should Be ", genderlist)
        gender = input("Enter Gender ").lower()

def calculations():
    global club
    if gender == "f" :
        if transport == "walk" :
            club = "science"
        else:
            club = "coding"

    if gender == "m" :
        if SATS > 4 :
            club = "debating"
        else:
            club = "coding"

def printing():
    print("Name ", firstname)
    print("Age ", age)
    print("SATS ", SATS)
    print("transport ", transport)
    print("gender ", gender)
    print("club ", club)
    

getdetails()
calculations()
printing()

    
