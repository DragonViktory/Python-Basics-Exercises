fruit = input()
day_of_the_week = input()
amount = float(input())
single_price = 0
total_price = 0

if day_of_the_week in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    if fruit == "banana":
        single_price = 2.50
    elif fruit == "apple":
        single_price = 1.20
    elif fruit == "orange":
        single_price = 0.85
    elif fruit == "grapefruit":
        single_price = 1.45
    elif fruit == "kiwi":
        single_price = 2.70
    elif fruit == "pineapple":
        single_price = 5.50
    elif fruit == "grapes":
        single_price = 3.85
elif day_of_the_week in ["Saturday", "Sunday"]:
    if fruit == "banana":
        single_price = 2.70
    elif fruit == "apple":
        single_price = 1.25
    elif fruit == "orange":
        single_price = 0.90
    elif fruit == "grapefruit":
        single_price = 1.60
    elif fruit == "kiwi":
        single_price = 3.00
    elif fruit == "pineapple":
        single_price = 5.60
    elif fruit == "grapes":
        single_price = 4.20
if day_of_the_week not in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] \
        or fruit not in ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]:
    print("error")
    exit()
total_price = single_price * amount
print(f"{total_price:.2f}")
