import sqlite3
def createtable():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    sqlCommand = """
    CREATE TABLE if not exists tblflight
    (
    flightno    TEXT,
    destin      TEXT,
    cost        FLOAT,
    passengers  INTEGER,
    primary key(flightno)
    )"""

    cursor.execute(sqlCommand)
    print("Table Created ")
    press = input("Press enter to continue ")
    conn.commit() #writes the table to the hard disk
    conn.close()

def insertdata():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()
    more = True
    while more :
        array = []
        flightno = input("Enter Flight Number ")
        destin = input("Enter Destination ")
        cost = int(input("Enter Cost "))
        passengers = input("Enter Passenger Number ")
        array.append(flightno)
        array.append(destin)
        array.append(cost)
        array.append(passengers)

        #cursor.execute("INSERT INTO tblflightno VALUES (?,?,?,?)", array)
        morefl = input("More Flights y / n ").lower()
        if morefl == "n":
            more = False
    conn.close()

def printdata():
    conn = sqlite3.connect("flights.db")
    cursor = conn.cursor()

    result = cursor.execute("select * from tblflight ")
    for eachRow in result:
        print(eachRow)

    conn.close()
    press = input("Press Enter To Continue ")

choice = 0

while choice !=4:
    print("1 Create Table ")
    print()
    print("2 Insert Data ")
    print()
    print("3 Print Data ")
    print()
    print("4 Exit ")

    choice = int(input("Enter Choice 1 - 4 "))
    if choice == 1:
        createtable()
    elif choice == 2:
        insertdata()
    elif choice == 3:
        printdata()

#100a Durban 600 200
#200x London 300 100
#300p Paris 250 300
#400x Brussels 400 200
#500 Johanesburg 700 300
