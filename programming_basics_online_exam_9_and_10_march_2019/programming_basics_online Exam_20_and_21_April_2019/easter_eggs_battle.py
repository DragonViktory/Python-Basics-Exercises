number_eggs_first = int(input())
number_eggs_second = int(input())
command = input()
egs_counter_first = number_eggs_first
egs_counter_second = number_eggs_second

while command != "End":
    if command == "one":
        egs_counter_second -= 1
        if egs_counter_second == 0:
            print(f"Player two is out of eggs. Player one has {egs_counter_first} eggs left.")
            exit(0)
    elif command == "two":
        egs_counter_first -= 1
        if egs_counter_first == 0:
            print(f"Player one is out of eggs. Player two has {egs_counter_second} eggs left.")
            exit(0)
    command = input()

print(f"Player one has {egs_counter_first} eggs left.")
print(f"Player two has {egs_counter_second} eggs left.")

