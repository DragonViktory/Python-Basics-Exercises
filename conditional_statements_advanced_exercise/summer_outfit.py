grade = int(input())
time_of_day = input()
outfit = ""
shoes = ""

if time_of_day == "Morning":
    if 10 <= grade <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif grade <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
    else:
        outfit = "T-Shirt"
        shoes = "Sandals"

elif time_of_day == "Afternoon":
    if 10 <= grade <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif grade <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    else:
        outfit = "Swim Suit"
        shoes = "Barefoot"
else:
    outfit = "Shirt"
    shoes = "Moccasins"
print(f"It's {grade} degrees, get your {outfit} and {shoes}.")