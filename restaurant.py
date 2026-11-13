print("Welcome to our restaurant!, Here's our menu: ")
menu = {"Pasta": 250, "Pizza": 300, "Burger": 150, "Salad": 200, "Sandwich": 220, "Fries": 120}

order = input("Please enter the items you would like to order:  ")

if order in menu:
    print(f"You have ordered {order}. The price is {menu[order]} rupees.")
else:
    print(f"Sorry, we don't have {order} right now.")
    
next_order = input("Would you like to order anything else? ")
if next_order == "yes":
    total1 = menu[order]
    second = input("Enter your second order: ")
    if second in menu:
        total = menu[order] + menu[second]
        print(f"Order of {second} is added. The total price to pay is {total} ")

    else:
        print(f"Sorry sir, we dont have {second} right now, your total bill is {total1} ")

else:
    print(f"Thanks sir pls visit us again")

