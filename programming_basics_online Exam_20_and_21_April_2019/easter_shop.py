start_number_eggs = int(input())
command = input()
sold_eggs_counter = 0
more_eggs = True
total_number_eggs = start_number_eggs

while command != "Close":
    current_number_eggs = int(input())
    if command == "Buy":
        if total_number_eggs < current_number_eggs:
            more_eggs = False
            break
        else:
            total_number_eggs -= current_number_eggs
            sold_eggs_counter += current_number_eggs
    else: # command == "Fill":
        total_number_eggs += current_number_eggs
    command = input()
if more_eggs:
    print("Store is closed!")
    print(f"{sold_eggs_counter} eggs sold.")
else:
    print("Not enough eggs in store!")
    print(f"You can buy only {total_number_eggs}.")



