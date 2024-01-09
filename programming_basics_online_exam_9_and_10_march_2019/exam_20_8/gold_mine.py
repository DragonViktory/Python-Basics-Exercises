number_of_locations = int(input())

for location in range(1, number_of_locations + 1):
    expected_average_gold = int(input())
    number_of_days_per_locations = int(input())
    current_gold = 0

    for day in range(1, number_of_days_per_locations + 1):
        gold_mined_per_day = int(input())
        current_gold += gold_mined_per_day
        average_gold_per_day = current_gold / number_of_days_per_locations
    if average_gold_per_day >= expected_average_gold:
        print(f"Good job! Average gold per day: {average_gold_per_day:.2f}.")
    else:
        difference = expected_average_gold - average_gold_per_day
        print(f"You need {abs(difference):.2f} gold.")
