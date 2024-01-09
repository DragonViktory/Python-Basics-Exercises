budget = float(input())
season = input()
location = ""

if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    else:  # season =="Winter":
        location = "Morocco"
        price = budget * 0.45
elif budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.80
    else:  # season =="Winter":
        location = "Morocco"
        price = budget * 0.60
else:  # budget > 3000
    accommodation = "Hotel"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.90
    else:  # season =="Winter":
        location = "Morocco"
        price = budget * 0.90
print(f"{location} - {accommodation} - {price:.2f}")
