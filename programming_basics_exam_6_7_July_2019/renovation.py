from math import ceil

wall_height = int(input())
wall_width = int(input())
percentage_no_paint = int(input())
command = input()
more_to_paint = True
current_liter = 0
volume_room = wall_height * wall_width * 4
target_painting = volume_room - ((volume_room * percentage_no_paint) / 100)
target_painting_rounded = ceil(target_painting)
current_painting = 0

while command != "Tired!":
    liter = int(command)
    current_liter += liter
    current_volume_left = target_painting_rounded - current_liter
    if current_volume_left < 0:
        more_to_paint = False
        break
    command = input()
if more_to_paint:
    print(f"{current_volume_left} quadratic m left.")
else:
    if current_liter > 0:
        print(f"All walls are painted and you have {abs(current_volume_left)} l paint left!")
    else:
        print("All walls are painted! Great job, Pesho!")