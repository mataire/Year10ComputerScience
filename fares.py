passlist = []
dufare = int(800)
nyfare = int(700)
def getdata():
    global destination, passlist
    name = input("Enter Name ")
    age = input("Enter Age ")
    kids = int(input("Enter Number Of Kids "))
    while kids > 3:
        print("Kids > 3 ")
        kids = int(input("Enter No of kids"))
    destination = input("Enter NY or DU ").lower()
    print("Destination ", destination)
    while destination != "ny" and destination != "du":
        print("NY or DU only ")
        destination = input("Enter NY or DU ").lower()
    passlist.append(name)
    passlist.append(destination)
    passlist.append(kids)
    print(passlist)

def calfare():
    print(passlist)
    if destination =="du":
        fare = dufare
        if passlist[2] > 0:
            kidsfare = passlist[2]*fare*3/4
            fare = fare + kidsfare
       
    if destination =="ny":
        fare = nyfare
        if passlist[2] > 0:
            kidsfare = passlist[2]*fare*3/4
            fare = fare + kidsfare
    print("Name ", passlist[0])
    if passlist[1] == "ny":
        print("Denstination: New York ")
    else:
        print("Destination: Durban ")
    print("Adult Fare ", (fare - kidsfare))
   # if passlist[2] > 0:
    print("Kids Fare ", kidsfare)
    
nm = int(input("Enter number of people "))
while nm < 0 or nm > 3:
    print("Number of people should be less than 4")
    nm = int(input("Enter number of people "))
for count in range(nm):
    getdata()
    calfare()

            
    