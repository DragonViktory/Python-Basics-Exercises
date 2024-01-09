first_number = int(input())
second_number = int(input())
third_number = int(input())
number1 = 0
number2 = 0
number3 = 0

for number1 in range(1, first_number + 1):
    for number2 in range(1, second_number + 1):
        for number3 in range(1, third_number + 1):
            if number3 % 2 == 0 and number1 % 2 == 0 and number2 in range(2, second_number + 1):
                if all(number2 % i != 0 for i in range(2, number2)):
                    print(f"{number1} {number2} {number3}")
