food_bought_kg = int(input())
food_gr = food_bought_kg * 1000
command = input()

while command != "Adopted":
    current_food = int(command)
    food_gr -= current_food
    command = input()

if food_gr >= 0:
    print(f"Food is enough! Leftovers: {food_gr} grams.")
else:
    print(f"Food is not enough. You need {abs(food_gr)} grams more.")
