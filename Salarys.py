def details():

    global firstname, gross, surname, age
    firstname = input("Enter Name ")
    surname = input("Enter Surname ")
    gross = float(input("Enter Gross "))
    age = int(input("Enter Age "))

def calculations():

    global tax, insurance

    if gross < 2000 :
        tax = 5/100 * gross

    elif gross < 4000:
        tax = 8/100 * gross

    else:
        tax = 0.1 * gross

    if gross < 2000 :
        insurance = 0.05 * gross

    else:
        insurance = 0.06 * gross


def printing():
    print("Name ", firstname "Surname ", surname)
    print("Gross ", gross "Age ", age)
    print("Tax ", tax "Insurance ", insurance)


getdetails()
calculations()
printing()
    
