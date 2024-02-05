genderlist = ["m", "f"]
gender = input("Enter Gender ").lower()
while gender not in genderlist :
    print("Gender Should Be ", genderlist)
    gender = input("Enter Gender ").lower()