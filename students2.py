import sqlite3
def createtable():
    conn = sqlite3.connect("students.db")#,"teachers.db")
    cursor = conn.cursor()
    sqlCommand = """
    CREATE TABLE if not exists tblstudents
    (
    studentid TEXT,
    name      TEXT,
    surname   TEXT,
    age       INTEGER,
    postcode  TEXT,
    primary key(studentid)

    )"""
    #CREATE TABLE if not exists tblteachers
    #(
    #teacherid TEXT,
    #title     TEXT,
    #namet     TEXT,
    #surnamet  TEXT,
    #subject   TEXT,
    #aget      INTEGER,
    #postcodet TEXT,
    #primary key(teacherid)
    #)"""

    cursor.execute(sqlCommand)
    print("Table Created ")
    press = input("Press enter to continue ")
    conn.commit() #writes the table to the hard disk
    conn.close()
def insertdata():#studentdata
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    more = True
    while more :
        array = []
        studentid = input("Enter Student ID ")
        name = input("Enter Name ")
        surname = input("Enter Surname ")
        age = int(input("Enter Age "))
        postcode = input("Enter Postcode ")
        array.append(studentid)
        array.append(name)
        array.append(surname)
        array.append(age)
        array.append(postcode)

        #cursor.execute("INSERT INTO tblstudents VALUES (?,?,?,?,?)", array)
        morestud = input("More Students y / n ").lower()
        if morestud == "n":
            more = False
    conn.close()

def insertteach():#teacherdata
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    more = True
    while more :
        array = []
        teacherid = input("Enter Teacher ID ")
        title = input("Enter Title ")
        namet = input("Enter Name ")
        surnamet = input("Enter Surname ")
        subject = input("Enter Subject ")
        aget = int(input("Enter Age "))
        array.append(teacherid)
        array.append(title)
        array.append(namet)
        array.append(surnamet)
        array.append(subject)
        array.append(aget)

        cursor.execute("INSERT INTO tblteachers VALUES (?,?,?,?,?)", array)
        moreteach = input("More Teachers y / n ").lower()
        if moreteach == "n":
            more = False
    conn.close()

def readdata():#self explain
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    result = cursor.execute("select * from tblstudents ")
    for eachRow in result:
        print(eachRow)

    result = cursor.execute("select * from tblteachers ")
    for eachRow in result:
        print(eachRow)

    conn.close()
    press = input("Press Enter To Continue ")

def searchrec():#self explain
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

choice = 0

while choice !=6:
    print("1 Create Table ")
    print()
    print("2 Insert Student Data ")
    print()
    print("3 Insert Teacher Data ")
    print()
    print("4 Read Data ")
    print()
    print("5 Search Rec ")
    print()
    print("6 Exit ")

    choice = int(input("Enter Choice 1 - 6 "))
    if choice == 1:
        createtable()
    elif choice == 2:
        insertdata()
    elif choice == 3:
        insertteach()
    elif choice == 4:
        readdata()
    elif choice == 5:
        searchrec()
