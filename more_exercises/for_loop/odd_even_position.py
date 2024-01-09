from sys import maxsize

number_of_numbers = int(input())
odd_sum = 0
odd_min = maxsize
odd_max = -maxsize
even_sum = 0
even_min = maxsize
even_max = -maxsize

sum_odd_min = 0
sum_odd_max = 0
sum_even_min = 0
sum_even_max = 0

for i in range(1, number_of_numbers + 1):
    number = float(input())

    if i % 2 == 0:
        even_sum += number
        if number < even_min:
            even_min = number
            sum_even_min += even_min
        if number > even_max:
            even_max = number
            sum_even_max += even_max
    else:
        odd_sum += number
        if number < odd_min:
            odd_min = number
            sum_odd_min += odd_min
        if number > odd_max:
            odd_max = number
            sum_odd_max += odd_max

if number_of_numbers == 0:
    print(f"OddSum={odd_sum:.2f}, ")
    print("OddMin=No, ")
    print(f"OddMax=No, ")
    print(f"EvenSum={even_sum:.2f}, ")
    print("EvenMin=No, ")
    print("EvenMax=No")
elif number_of_numbers == 1:
    print(f"OddSum={odd_sum:.2f}, ")
    print(f"OddMin={odd_min:.2f}, ")
    print(f"OddMax={odd_max:.2f}, ")
    print(f"EvenSum={even_sum:.2f}, ")
    print("EvenMin=No, ")
    print("EvenMax=No")
else:
    print(f"OddSum={odd_sum:.2f}, ")
    print(f"OddMin={odd_min:.2f}, ")
    print(f"OddMax={odd_max:.2f}, ")
    print(f"EvenSum={even_sum:.2f}, ")
    print(f"EvenMin={even_min:.2f}, ")
    print(f"EvenMax={even_max:.2f}")
