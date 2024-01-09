first_number = int(input())
number1 = 0
number2 = 0
number3 = 0
number4 = 0

for number1 in range(1, 10):
    for number2 in range(1, 10):
        for number3 in range(1, 10):
            for number4 in range(1, 10):
                if number1 + number2 == number3 + number4 and first_number % (number1 + number2) == 0:
                    print(f"{number1}{number2}{number3}{number4}", end=" ")
