def getdata():
    global pd, pt, cost, qty, pm
    more = True
    while more:
        print("Welcome To Waitrose ")
        pd = input("Enter product desc ")
        pt = input("Enter product type ")
        cost = input("Enter Cost")
        while not cost.isdigit() or int(cost) > 20:
            print("Item should be less than £20 ")
            cost = input("Enter Cost ")
        cost = int(cost)
        qty = int(input("Enter Quantity "))
        pm = input("Payment Method ").lower()
        while pm != "cash" and pm != "card" :
            print("Should be cash or card ")
            pm = input("Enter payment method ")
        
        mi = input("More Items ? ").lower()
        if mi == "n":
            more = False
        else:
            more = True
        
        
def process():
    global total, vat, cc, discount, money, change
    
    
    total = cost * qty
    vat = total * 0.2
    if pm == "card":
        cc = 5/100 * total
    else:
        cc = 0
        
    if pd == "clothes ":
        discount = 2/100 * total
    elif pd == "grocery ":
        discount = 4/100 * total
    else:
        discount = 5/100 * total
        
    nt = total - discount
    
    money = int(input("Enter Amount"))

    
    if money < nt:
        print("Not enough Money ")
    else:
        change = money - nt
    
def printing():
    print("Product Desc ", pd)
    print("Product Type ", pt)
    print("Cost ", cost)
    print("Quantity ", qty)
    print("Payment Method", pm)
    print("Change ", change)
    print("Discount", discount)
    print("VAT ",vat)

getdata()
process()
printing()
    
    
    