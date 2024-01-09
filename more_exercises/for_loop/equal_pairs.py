couple_numbers = int(input())
max_couple_value = 0
max_difference_value = 0
same_couples = 0
for number in range(couple_numbers):
    first_number = int(input())
    second_number = int(input())
    current_couple_value = first_number + second_number
    if current_couple_value > max_couple_value:
        if max_difference_value > current_couple_value:
            max_difference_value = current_couple_value
        max_difference_value = current_couple_value - max_couple_value
        max_couple_value = current_couple_value
    elif current_couple_value < max_couple_value:
        if max_difference_value > current_couple_value:
            max_difference_value = current_couple_value
        max_difference_value = current_couple_value - max_couple_value
        max_couple_value = current_couple_value
    else:
        same_couples += 1
if same_couples+1 == couple_numbers:
    print(f"Yes, value={max_couple_value}")
else:
    print(f"No, maxdiff={abs(max_difference_value)}")









