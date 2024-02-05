import sqlite3
def createtable():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    sqlCommand = """
    CREATE TABLE if not exists tblstudents
    (
    studentid TEXT,
    name      TEXT,
    age       INTEGER,
    postcode  TEXT,
    primary key(studentid)
    )"""

    cursor.execute(sqlCommand)
    print("Table Created ")
    press = input("Press enter to continue ")
    conn.commit() #writes the table to the hard disk
    conn.close()
def insertdata():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    more = True
    while more :
        array = []
        studentid = input("Enter Student ID ")
        name = input("Enter Name ")
        age = int(input("Enter Age "))
        postcode = input("Enter Postcode ")
        array.append(studentid)
        array.append(name)
        array.append(age)
        array.append(postcode)

        cursor.execute("INSERT INTO tblstudents VALUES (?,?,?,?)", array)
        morestud = input("More Students y / n ").lower()
        if morestud == "n":
            more = False
    conn.close()

def readdata():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    result = cursor.execute("select * from tblstudents ")
    for eachRow in result:
        print(eachRow)

    conn.close()
    press = input("Press Enter To Continue ")

def searchrec():
    conn = sqlite3.connect("students.db")
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

