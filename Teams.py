def getdetails():
    global name, age, i, gender, football, netball, tennis, other

    name = input("Enter Name ")
    age = int(input("Enter Age "))
    i = input("Enter Your Interests ( football, netball, tennis, other ) ")
    gender = input("Enter Gender ( m / f / o)" )

def calculations():
    global group, team

    if gender == "m" :
        if i == "football" or "other" :
            group = "Group 1 "

    if gender == "f" :
        if i == "football" or "other" :
            group = "Group 1 "

    if gender == "m" :
        if i == "netball" or "tennis" :
            group = "Group 2 "

    if gender == "f" :
        if i == "netball" or "tennis" :
            group = "Group 3 "

    if gender == "o" :
        group = "Group 2 "

    if group == "Group 1" or "Group 2" :
        team = "Team 1"
    else:
        team = "Team 2"

def printing():

    print("Name ", name)
    print("Age ", age)
    print("Interests ", i)
    print("Gender ", gender)
    print("Group ", group
    print("Team ", team)
    
            
getdetails()
calculations()
printing()
