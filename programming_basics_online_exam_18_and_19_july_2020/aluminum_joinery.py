number_of_windows = int(input())
kind_of_windows = input()
delivery = input()

if number_of_windows < 10:
    print("Invalid order")
    exit()

if kind_of_windows == "90X130":
    single_price = 110
    if number_of_windows > 60:
        single_price *= 0.92
    elif number_of_windows > 30:
        single_price *= 0.95

elif kind_of_windows == "100X150":
    single_price = 140
    if number_of_windows > 80:
        single_price *= 0.90
    elif number_of_windows > 40:
        single_price *= 0.94

elif kind_of_windows == "130X180":
    single_price = 190
    if number_of_windows > 50:
        single_price *= 0.88
    elif number_of_windows > 20:
        single_price *= 0.93

elif kind_of_windows == "200X300":
    single_price = 250
    if number_of_windows > 50:
        single_price *= 0.86
    elif number_of_windows > 25:
        single_price *= 0.91

total_price = single_price * number_of_windows
if delivery == "With delivery":
    total_price += 60
if number_of_windows > 99:
    total_price = total_price - (total_price * 0.04)


print(f"{total_price:.2f} BGN")



