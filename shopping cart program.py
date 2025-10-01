food = []
price = []
tot = 0

while True:
    food_item = input("Enter a food item (q to quit):")
    if food_item.lower() == "q":
        break

    else:
        price_item = float(input(f"Enter the price of a {food_item}: $"))
        food.append(food_item)
        price.append(price_item)
        tot += price_item
        print(f"cart has {food}, your total is ")

print(f"""You have 
{food}
in your cart
Your total is ${tot:.2f}""")
