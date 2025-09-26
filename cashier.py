item = input("what would you like to buy?: ")
price = float(input("what is the price?: "))
quantity = int(input(f"how many {item} would you like to buy?: "))
total = price * quantity

print(f"your total is: {total}")
