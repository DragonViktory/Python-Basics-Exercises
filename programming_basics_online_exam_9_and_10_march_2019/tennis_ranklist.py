number_of_tournaments = int(input())
starting_points = int(input())
total_points = starting_points
current_points = 0
w_counter = 0
f_counter = 0
sf_counter = 0

for _ in range(number_of_tournaments):
    tournament_stage_reached = input()
    if tournament_stage_reached == "W":
        w_counter += 1
        current_points += 2000
    if tournament_stage_reached == "F":
        f_counter +=1
        current_points += 1200
    if tournament_stage_reached == "SF":
        sf_counter += 1
        current_points += 720
average_points = int(current_points / number_of_tournaments)
total_points = current_points + total_points
percentage_won = w_counter/ number_of_tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percentage_won:.2f}%")