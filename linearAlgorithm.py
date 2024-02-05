#linear search Algorithm

import random

numbers = []

for count in range(12) :
    num = random.randint(10,50)
    numbers.append(num)
print(numbers)

count = 0
found = False

def linear(se):
    global count, found
    while se != numbers[count] and count < len(numbers) - 1:
        count = count + 1
    if se == numbers[count]:
        found = True
        print("Search ", se, "Found at ", count)

search = int(input("Enter Number To Search "))
linear(search)
if not found:
    print("Element Not Found ")

                 
