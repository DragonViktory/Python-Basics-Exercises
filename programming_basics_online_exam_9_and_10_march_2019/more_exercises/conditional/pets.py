from math import ceil, floor

number_of_days = int(input())
left_food_kg = int(input())
food_per_day_dog_kg = float(input())
food_per_day_kat_kg = float(input())
food_per_day_turtle_gr = float(input())

total_food = number_of_days * (food_per_day_dog_kg + food_per_day_kat_kg + food_per_day_turtle_gr / 1000)
difference = abs(left_food_kg - total_food)

if left_food_kg >= total_food:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")


