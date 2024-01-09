number_of_detergent_bottles = int(input())
counter = 0
total_dishes = 0
total_pots = 0
detergent = number_of_detergent_bottles * 750


while detergent >= 0:
    command = input()
    if command == "End":
        break
    dishes = int(command)

    counter += 1

    if counter %3 == 0:
        total_pots += dishes
        detergent -= dishes * 15
    else:
        total_dishes += dishes
        detergent -= dishes * 5


if detergent < 0:
    print(f"Not enough detergent, {-detergent} ml. more necessary!")
else:
    print("Detergent was enough!")
    print(f"{total_dishes} dishes and {total_pots} pots were washed.")
    print(f"Leftover detergent {detergent} ml.")


