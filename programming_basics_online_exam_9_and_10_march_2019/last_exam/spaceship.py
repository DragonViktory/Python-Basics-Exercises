import math

width_spaceship = float(input())
length_spaceship = float(input())
height_spaceship = float(input())
average_height_astronauts = float(input())
volume_spaceship = width_spaceship * length_spaceship * height_spaceship
room_volume = (average_height_astronauts + 0.40) * 2 * 2
astronauts_counter = math.floor(volume_spaceship / room_volume)

if 0 < astronauts_counter < 3:
    print(f"The spacecraft is too small.")
elif astronauts_counter <= 10:
    print(f"The spacecraft holds {astronauts_counter} astronauts.")
else:
    print("The spacecraft is too big.")
