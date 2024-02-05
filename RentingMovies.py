def getdetails():
    global movietitle, classification, genre, nom
    
    movietitle = input("Enter Movie Title ")
    classification = input("Enter Movie Classification ")
    nom = int(input("Enter number of movies you want to rent "))#.lower()
    genrelist = ["comedy", "war", "drama", "horror", "kids"]
    genre = input("Enter genre ").lower()
    while genre not in genrelist :
        print("Gender Should Be ", genrelist)
        genre = input("Enter genre ").lower()
        

def calculations():
    global rentprice, rentaldate, total

    if genre == "comedy" or "war" :
        rentprice = 10 * nom
        rentaldate = 12
    else:
        print("Wrong Movie ")

    if genre == "kids" :
        rentprice = 6 * nom
        rentaldate = 6
    if genre == "drama" or "horror" :
        rentprice = 8 * nom
        rentaldate = 10

    total = rentprice + rentaldate

def printdetails():

    print("Movie title ", movietitle)
    print("Classification ", classification)
    print("Genre ", genre)
    print("Number Of Movies ", nom)
    print("Rental Cost ", rentprice)
    print("Rental Period ", rentaldate)
    print("Total ", total)

getdetails()
calculations()
printdetails()

    
        
    
        
        
    
    
