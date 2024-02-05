names = []
sats = []
emarks = []


for count in range(3) :
    name = input("Enter Name ")
    sat = int(input("Enter SATS Result "))
    emark = int(input("Enter English Mark "))
    names.append(name)
    sats.append(sat)
    emarks.append(emark)

print(name)
print(sat)
print(emarks)

if names == "jack" :
    print("Jack Found!")
    print(names, "jack")
    print(sats, "jack")
    print(emarks, "jack")

#total = 0
#totals = []

#for count in sats :
    #totals = total + sats[count]

#for count in emarks :
    #totals = total + emarks[count]

totalsat = sat + sat + sat
totaleng = emark + emark + emark
print("SATS Total", totalsat)
print("English Total", totaleng)

#print(total)
#print(totals)

