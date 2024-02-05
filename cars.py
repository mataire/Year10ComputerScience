cars = []
values = []
years = []

for count in range(4) :
    car = input("Enter Car ")
    value = float(input("Enter Value "))
    year = int(input("Enter Year "))
    cars.append(car)
    values.append(value)
    years.append(year)
    
print(cars)
print(values)
print(years)

newlist = []

for x in range(4):
    if values[x] > 1999 :
        newlist.append(cars[x])
        newlist.append(values[x])
        newlist.append(years[x])

print(newlist)