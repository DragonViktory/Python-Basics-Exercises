fruit = input()
size_set = input()
number_of_sets = int(input())

small_set = 2
big_set = 5

if fruit == "Watermelon":
    if size_set == "small":
        price = 56 * small_set
    elif size_set == "big":
        price = 28.70 * big_set
elif fruit == "Mango":
    if size_set == "small":
        price = 36.66 * small_set
    elif size_set == "big":
        price = 19.60 * big_set
elif fruit == "Pineapple":
    if size_set == "small":
        price = 42.10 * small_set
    elif size_set == "big":
        price = 24.80 * big_set
elif fruit == "Raspberry":
    if size_set == "small":
        price = 20 * small_set
    elif size_set == "big":
        price = 15.20 * big_set
current_sum = number_of_sets * price
if current_sum < 400:
    total_sum = current_sum
elif current_sum <= 1000:
    total_sum = current_sum * 0.85
else:
    total_sum = current_sum * 0.50
print(f"{total_sum:.2f} lv.")
