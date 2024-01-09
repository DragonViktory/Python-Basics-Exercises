hour = int(input())
minutes = int(input())

new_time_seconds = (hour * 60) + minutes + 15

new_hour = new_time_seconds // 60
new_minutes = new_time_seconds % 60

if new_hour > 23:
    new_hour = 0
if new_minutes < 10:
    print(f"{new_hour}:0{new_minutes}")
else:
    print(f"{new_hour}:{new_minutes}")
