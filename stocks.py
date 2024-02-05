import sqlite3
def createtable():
    conn = sqlite3.connect("stock.db")
    cursor = conn.cursor()
    sqlCommand = """
    CREATE TABLE if not exists tblstocks
    (
    stockid   TEXT,
    Descr     TEXT,
    Cost      INTEGER,
    qty       INTEGER,
    country   TEXT,
    countryc  TEXT,
    primary key(stockid)
    )"""

    cursor.execute(sqlCommand)
    print("Table Created ")
    press = input("Press enter to continue ")
    conn.commit() #writes the table to the hard disk
    conn.close()
def insertdata():
    conn = sqlite3.connect("stock.db")
    cursor = conn.cursor()
    more = True
    while more :
        array = []
        stockid = input("Enter Stock ID ")
        descr = input("Enter Item Name ")
        cost = int(input("Enter Cost "))
        qty = int(input("Enter Amount "))
        country = input("Enter Coutry ")
        countryc = input("Enter Country Code ")
        array.append(stockid)
        array.append(descr)
        array.append(cost)
        array.append(qty)
        array.append(country)
        array.append(countryc)

        cursor.execute("INSERT INTO tblstocks VALUES (?,?,?,?,?,?)", array)
        morestock = input("More Stock y / n ").lower()
        if morestock == "n":
            more = False
    print(array)
    conn.close()

def readdata():
    conn = sqlite3.connect("stock.db")
    cursor = conn.cursor()

    result = cursor.execute("select * from tblstocks where qty > 300")
    for eachRow in result:
        print(eachRow)

    results = cursor.execute("select * from tblstocks where cost < 2")
    for eachRow in result:
        print(eachRow)

    print(tblstocks)

    conn.close()
    press = input("Press Enter To Continue ")

def searchrec():
    conn = sqlite3.connect("stock.db")
    cursor = conn.cursor()

choice = 0

while choice !=5:
    print("1 Create Table ")
    print()
    print("2 Insert Data ")
    print()
    print("3 Read Data ")
    print()
    print("4 Search Rec ")
    print()
    print("5 Exit ")

    choice = int(input("Enter Choice 1 - 5 "))
    if choice == 1:
        createtable()
    elif choice == 2:
        insertdata()
    elif choice == 3:
        readdata()
    elif choice == 4:
        searchrec()
