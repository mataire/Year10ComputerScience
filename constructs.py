def selection():
    gender = input("Gender ").lower()
    age = int(input("Age "))
    
    if gender == "f":
        if age < 13:
            print("Young Female ")
        else:
            print("Old Female ")
    else:
        print("Not Female ")
        
#selection()
        
num = int(input("Enter Number Of Students "))
def count_control():
    name = input("Name ")
    age = input("Age ")
    print("Name ", name, "Age ", age)
    
for count in range (num):
    count_control()