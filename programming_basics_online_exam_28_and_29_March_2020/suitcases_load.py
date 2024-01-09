capacity = float(input())
suitcases_count = 0

while True:
    command = input()

    if command == "End":
        print("Congratulations! All suitcases are loaded!")
        break

    suitcase_volume = float(command)
    suitcases_count += 1

    if suitcases_count % 3 == 0:
        suitcase_volume += suitcase_volume * 0.10

    if suitcase_volume > capacity:
        print("No more space!")
        suitcases_count -= 1
        break

    capacity -= suitcase_volume

print(f"Statistic: {suitcases_count} suitcases loaded.")
