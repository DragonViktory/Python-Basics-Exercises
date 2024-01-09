number_of_eastern_cakes = int(input())
best_becker = ""
max_points = 0

for cake in range(number_of_eastern_cakes):
    total_points = 0
    name_backer = input()
    current_points_backer = input()
    while current_points_backer != "Stop":
        points_integer = int(current_points_backer)
        total_points += points_integer
        current_points_backer = input()
    print(f" {name_backer} has {total_points} points.")
    if total_points > max_points:
        best_becker = name_backer
        max_points = total_points
        print(f"{name_backer} is the new number 1!")
print(f"{best_becker} won competition with {max_points} points!")
