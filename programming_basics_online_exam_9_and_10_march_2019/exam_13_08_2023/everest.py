command = input()
target_meters = 8848
current_meters = 5364
nights = 0

while nights <= 5 and current_meters < 8848 and command != "END":
    if command == "Yes":
        climbed_meters = int(input())
        current_meters += climbed_meters
        nights += 1
    elif command == "No":
        climbed_meters = int(input())
        current_meters += climbed_meters

    command = input()

if current_meters > 8848:
    print(f"Goal reached for {nights} days!")
elif current_meters == 8848:
    print(f"Goal reached for {nights} days!")
else:
    print("Failed!")
    print(f"{current_meters}")
