from math import ceil
number_breads = int(input())
packets_of_sugar = 950
packets_of_flour = 750
current_sugar = 0
current_flour = 0
max_grams_sugar = 0
max_grams_flour = 0

for _ in range(number_breads):
    amount_sugar_grams = int(input())
    amount_sugar_flour = int(input())
    if amount_sugar_grams > max_grams_sugar:
        max_grams_sugar = amount_sugar_grams
    if amount_sugar_flour > max_grams_flour:
        max_grams_flour = amount_sugar_flour
    current_sugar += amount_sugar_grams
    current_flour += amount_sugar_flour
packages_needed_sugar= ceil(current_sugar / 950)
packages_needed_flour = ceil(current_flour / 750)


print(f"Sugar: {packages_needed_sugar}")
print(f"Flour: {packages_needed_flour}")
print(f"Max used flour is {max_grams_flour} grams, max used sugar is {max_grams_sugar} grams.")
