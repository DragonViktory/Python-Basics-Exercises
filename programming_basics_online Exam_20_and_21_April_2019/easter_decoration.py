number_customers = int(input())
total_price = 0

for customers in range(1, number_customers+1):
    current_items = 0
    current_price = 0
    command = input()
    while command != "Finish":
        item = str(command)
        if item == "basket":
            current_price += 1.50
        elif item == "wreath":
            current_price += 3.80
        else:  # items == "chocolate bunny":
            current_price += 7
        current_items += 1
        command = input()
    if current_items % 2 == 0:
        current_price *= 0.80
    total_price += current_price
    print(f"You purchased {current_items} items for {current_price:.2f} leva.")

average_money = total_price / number_customers
print(f"Average bill per client is: {average_money:.2f} leva.")
