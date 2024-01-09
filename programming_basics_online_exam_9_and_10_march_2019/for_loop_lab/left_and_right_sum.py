count_of_numbers = int(input())
left_sum = 0
right_sum = 0
for numbers in range(count_of_numbers ** 2):
    current_number = int(input())
    if numbers < count_of_numbers:
        print(f"Before middle: {numbers}")
    else:
        print(f"After middle: {numbers}")
