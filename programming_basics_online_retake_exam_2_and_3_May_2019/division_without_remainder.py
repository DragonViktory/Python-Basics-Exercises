numbers = int(input())
number_divisible_by_two = 0
number_divisible_by_three = 0
number_divisible_by_four = 0

for num in range(numbers):
    number = int(input())
    if number % 2 == 0:
        number_divisible_by_two += 1
    if number % 3 == 0:
        number_divisible_by_three += 1
    if number % 4 == 0:
        number_divisible_by_four += 1

percentage_number_divisible_by_two = number_divisible_by_two / numbers * 100
percentage_divisible_by_three = number_divisible_by_three / numbers * 100
percentage_divisible_by_four = number_divisible_by_four/ numbers * 100

print(f"{percentage_number_divisible_by_two:.2f}%")
print(f"{percentage_divisible_by_three:.2f}%")
print(f"{percentage_divisible_by_four:.2f}%")
