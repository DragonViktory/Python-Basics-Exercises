number_eggs = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_element = 0

for egg in range(number_eggs):
    color_eggs = input()
    if color_eggs == "red":
        red_eggs += 1
    elif color_eggs == "orange":
        orange_eggs += 1
    elif color_eggs == "blue":
        blue_eggs += 1
    elif color_eggs == "green":
        green_eggs += 1

if red_eggs > max_element:
    max_element = red_eggs
    color = "red"
if orange_eggs > max_element:
    max_element = orange_eggs
    color = "orange"
if blue_eggs > max_element:
    max_element = blue_eggs
    color = "blue"
if green_eggs > max_element:
    max_element = green_eggs
    color = "green"


print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_element} -> {color}")
