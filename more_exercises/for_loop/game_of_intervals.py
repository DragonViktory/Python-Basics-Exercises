movements_game = int(input())
invalid_numbers = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
current_points = 0


for numbers in range(movements_game):
    number = int(input())
    if number < 0:
        invalid_numbers += 1
        current_points /= 2
    elif number <= 9:
        from_0_to_9 += 1
        current_points += number * 0.20
    elif number <= 19:
        from_10_to_19 += 1
        current_points += number * 0.30
    elif number <= 29:
        from_20_to_29 += 1
        current_points += number * 0.40
    elif number <= 39:
        from_30_to_39 += 1
        current_points += 50
    elif number <= 50:
        from_40_to_50 += 1
        current_points += 100
    elif number > 50:
        invalid_numbers += 1
        current_points /= 2

percentage_invalid_numbers = invalid_numbers/ movements_game * 100
percentage_from_0_to_9 = from_0_to_9/ movements_game * 100
percentage_from_10_to_19 = from_10_to_19/ movements_game * 100
percentage_from_20_to_29 = from_20_to_29/ movements_game * 100
percentage_from_30_to_39 = from_30_to_39/ movements_game * 100
percentage_from_40_to_50 = from_40_to_50/ movements_game * 100

print(f"{current_points:.2f}")
print(f"From 0 to 9: {percentage_from_0_to_9:.2f}%")
print(f"From 10 to 19: {percentage_from_10_to_19:.2f}%")
print(f"From 20 to 29: {percentage_from_20_to_29:.2f}%")
print(f"From 30 to 39: {percentage_from_30_to_39:.2f}%")
print(f"From 40 to 50: {percentage_from_40_to_50:.2f}%")
print(f"Invalid numbers: {percentage_invalid_numbers:.2f}%")

