upper_limit_first_number = int(input())
upper_limit_second_number = int(input())
upper_limit_third_number = int(input())

for number1 in range(1, upper_limit_first_number + 1):
    for number2 in range(2, upper_limit_second_number + 1):
        for number3 in range(1, upper_limit_third_number + 1):
            if number1 % 2 == 0 and number3 % 2 == 0 and number2 in range(2, upper_limit_second_number + 1):
                if all(number2 % i != 0 for i in range(2, number2)):
                    print(f"{number1} {number2} {number3}")
