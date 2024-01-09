length = int(input())
width = int(input())
height = int(input())
percent = float(input())
# 1 dm = 10 cm
# 10**3 = 1000
volume_aquarium = length * width * height * 0.001
space_occupied = volume_aquarium * percent/100
liters_needed = volume_aquarium - space_occupied
print(liters_needed)


