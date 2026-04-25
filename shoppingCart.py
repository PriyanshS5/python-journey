import random


item = input("What would you like to buy? ")
price = round(random.uniform(1, 9999), 2)   #this give the random float number from 1 - 9999 and rounding the decimal number to 2 decimals.
quantity = float (input("Mention the quantity: "))
print(f"The price is: {price}")

ready = input("Should I proceed for billing? ").lower()

if ready == "yes":
    total = quantity * price
    print(f"The item: {item} and the quantity would cost you ₹{total} totally.")
else:
    print("Ok! Have a nice day.")