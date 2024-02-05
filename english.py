names = []
english = []
maths = []

for x in range(4) :
    name = input("Enter Name ")
    englis = int(input("Enter English Score "))
    math = int(input("Enter Maths Score "))
    names.append(name)
    english.append(englis)
    maths.append(math)

print(names)
print(english)
print(maths)

totals = []

for x in range(4) :
    total = english[x] + maths[x]
    totals.append(total)

print(totals)
