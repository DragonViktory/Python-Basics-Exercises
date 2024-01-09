number_of_days = int(input())
total_amount_food = float(input())
current_dog_food = 0
current_cat_food = 0
amount_cookies = 0
for day in range(1, number_of_days + 1):
    amount_dog_food = int(input())
    amount_cat_food = int(input())
    current_dog_food += amount_dog_food
    current_cat_food += amount_cat_food
    total_food_eaten = current_dog_food + current_cat_food
    if day % 3 == 0:
        amount_cookies += (amount_dog_food + amount_cat_food) * 0.10
amount_cookies = round(amount_cookies)
percentage_eaten_food = total_food_eaten/ total_amount_food * 100
percentage_eaten_food_cat = current_cat_food / total_food_eaten * 100
percentage_eaten_food_dog = current_dog_food / total_food_eaten * 100

print(f"Total eaten biscuits: {amount_cookies}gr.")
print(f"{percentage_eaten_food:.2f}% of the food has been eaten.")
print(f"{percentage_eaten_food_dog:.2f}% eaten from the dog.")
print(f"{percentage_eaten_food_cat:.2f}% eaten from the cat.")
