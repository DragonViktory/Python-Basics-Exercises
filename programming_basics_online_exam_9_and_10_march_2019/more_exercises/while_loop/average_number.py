number = int(input())
current_sum = 0

for current_number in range(number):
    count_numbers = int(input())
    current_sum += count_numbers

average_number = current_sum / number
print(f"{average_number:.2f}")
