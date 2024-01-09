actor_name = input()
start_points = float(input())
number_assessors = int(input())
total_points = start_points

for current_grade in range(number_assessors):
    name_assessor = input()
    points_assessor = float(input())
    current_points = len(name_assessor) * points_assessor / 2
    total_points += current_points
    if total_points > 1250.5:
        break
if total_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
else:
    difference = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")