start_range = int(input())
end_range = int(input())
magic_number = int(input())
num1 = 0
num2 = 0
counter = 0
is_found = False

for num1 in range(start_range, end_range + 1):
    for num2 in range(start_range, end_range + 1):
        counter += 1
        if num1 + num2 == magic_number:
            print(f"Combination N:{counter} ({num1} + {num2} = {magic_number})")
            is_found = True
            break
    if is_found:
        break
if not is_found:
    print(f"{counter} combinations - neither equals {magic_number}")


