number_mens = int(input())
number_women = int(input())
max_tables = int(input())

number1 = 0
number2 = 0
number3 = 0
couple_list = []

for number2 in range(1, number_mens + 1):
    for number3 in range(1, number_women + 1):
        couple = f"({number2} <-> {number3})"
        if couple not in couple_list and len(couple_list) < max_tables:
            couple_list.append(couple)
            print(f"({number2} <-> {number3})", end=" ")
