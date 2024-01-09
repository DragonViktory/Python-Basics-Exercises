budget = float(input())
command = input()
product_counter = 0
current_price = 0
enough_money = True

while command != "Stop":
    price = float(input())
    product_counter += 1
    if product_counter % 3 == 0:
        price /= 2
    budget = budget - price
    if budget < 0:
        enough_money = False
        break
    current_price = current_price + price
    command = input()

if enough_money:
    print(f"You bought {product_counter} products for {current_price:.2f} leva.")
else:
    print("You don't have enough money!")
    print(f"You need {abs(budget):.2f} leva!")
