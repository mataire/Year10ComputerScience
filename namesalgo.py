#linear search on names Algorithm

import random

names = ["Kevin", "Ben", "Zuzanna", "Charlie", "Macsen"]

count = 0
found = False

def linear(se):
    global count, found
    while se != names[count] and count < len(names) - 1:
        count = count + 1
    if se == names[count]:
        found = True
        print("Search ", se, "Found at ", count)

search = input("Enter Names To Search ")
linear(search)
if not found:
    print("Element Not Found ")
