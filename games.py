def getdata():
    global name, age, interests, gender
    
    interests = input("Enter Interests - f for football, n for netball, t for tennis, v for volleyball ")
    name = input("Enter Full Name ")
    age = input("Enter Age ")
    gender = input("Enter Your Gender ")
    
def process():
    global team, group
    group = 0
    if gender == "m" or gender == "o" and interests == "f":
        group = 1
    if gender == "f" or gender == "o" and interests == "f":
        group = 1
    if gender == "m" and interests == "t" or interests == "n":
        group = 2
    if gender == "f" and interests == "t" or interests == "v":
        group = 1
    if gender == "o":
        group = 3
    if gender == "m" or gender == "f" and group == 0 :
        group = 4
    if group == 1 or group == 2:
        team = 1
    else:
        team = 2
        
def printing():
    print("Name ", name)
    print("Age ", age)
    print("Interests ", interests)
    print("Gender ", gender)
    print("Group ", group)
    print("Team ", team)
    
getdata()
process()
printing()