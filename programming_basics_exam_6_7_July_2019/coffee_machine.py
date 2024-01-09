drunk = input()
option = input()
number_of_drinks = int(input())

if drunk == "Espresso" and number_of_drinks >= 5:
    if option == "Without":
        price = 0.90
        price *= 0.65
        price *= 0.75
    elif option == "Normal":
        price = 1.00
        price *= 0.75
    elif option == "Extra":
        price = 1.20
        price *= 0.75
else:
    if option == "Without":
        price = 0.90
        price *= 0.75
    elif option == "Normal":
        price = 1.00
    elif option == "Extra":
        price = 1.20
if drunk == "Cappuccino":
    if option == "Without":
        price = 1.00
        price *= 0.65
    elif option == "Normal":
        price = 1.20
    elif option == "Extra":
        price = 1.60
if drunk == "Tea":
    if option == "Without":
        price = 0.50
        price *= 0.65
    elif option == "Normal":
        price = 0.60
    elif option == "Extra":
        price = 0.70

total_price = number_of_drinks * price
if total_price > 15:
    total_price *= 0.80

print(f"You bought {number_of_drinks} cups of {drunk} for {total_price:.2f} lv.")
