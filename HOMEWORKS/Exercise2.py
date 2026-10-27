# Shopping cart program

item = input("Enter the item you would like to buy: ")
price = float(input("What is the price: £"))
quantity = int(input("How many items do you need: "))

total = price*quantity

print(f"You have bought {quantity} {item}'s ")
print(f'Your total is £{total}')