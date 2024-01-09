import math

time_action = int(input())
count_scenes = int(input())
time_one_scene = int(input())

field_preparation = time_action * 0.15
time_filming = count_scenes * time_one_scene
needed_time = field_preparation + time_filming
difference = abs(needed_time - time_action)
difference = math.ceil(difference)

if needed_time > time_action:
    print(f"Time is up! To complete the movie you need {difference} minutes.")
elif needed_time < time_action:
    print(f"You managed to finish the movie on time! You have {difference} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {difference} minutes.")
