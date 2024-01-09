number_start_range = int(input())
number_end_range = int(input())
number1 = 0
number2 = 0
number3 = 0
number4 = 0

for number1 in range(number_start_range, number_end_range + 1):
    for number2 in range(number_start_range, number_end_range + 1):
        for number3 in range(number_start_range, number_end_range + 1):
            for number4 in range(number_start_range, number_end_range + 1):
                if number1 % 2 == 0 and number4 % 2 != 0 or number1 % 2 != 0 and number4 % 2 == 0:
                    if number1 > number4:
                        if (number2 + number3) % 2 == 0:
                            print(f"{number1}{number2}{number3}{number4}", end=" ")
