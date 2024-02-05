import sqlite3
def getdata():
    conn = sqlite3.connect("mac.db")
    cursor = conn.cursor()
    sqlCommand = """
       CREATE TABLE if not exists mactbl
       (
       itemid TEXT,
       descr  TEXT,
       qty    INTEGER,
       cost   INTEGER,
       primary key (itemid)
       ) """
    cursor.execute(sqlCommand)
    conn.commit() #writes to the database
    print("Mac Table Created ")
    conn.close()   

def buyitems():
    conn = sqlite3.connect("mac.db")
    cursor = conn.cursor()
    more = True
    while more:
        item = input("Enter Item ID ")
        sqlCommand = "SELECT * FROM mactbl where itemid = '%s' " % (item)
        result = cursor.execute(sqlCommand)
        found = False
        for rec in result:
            if rec[0]!= "   ":
                qty = int(input("Enter Quantity "))
                total = 0
                total = qty * int(rec[3])
                print("Total is ", total)
                money = int(input("Enter Money "))
                change = money - total
                print("Money ", money)
                print("Change ", change)
                
                morefood = input("More Food? y / n ").lower()
                if morefood == "n":
                    more = False
    conn.close()

#menu

choice = 0
while choice !=3:
    print("        Welcome to Mcdonalds ")
    print()
    print("1       Add food to the menu ")
    print()
    print("2       Buy food ")
    print()
    print("3       Exit ")
    print()
    choice = int(input("Enter Choice "))
    if choice == 1 :
        getdata()
    elif choice == 2:
        buyitems()
