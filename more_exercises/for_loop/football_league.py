capacity_of_the_stadium = int(input())
number_of_all_fans = int(input())
fans_a = 0
fans_b = 0
fans_v = 0
fans_g = 0

for fan in range(number_of_all_fans):
    sector = input()
    if sector == "A":
        fans_a += 1
    elif sector == "B":
        fans_b += 1
    elif sector == "V":
        fans_v += 1
    elif sector == "G":
        fans_g += 1

percentage_fans_a = fans_a/number_of_all_fans * 100
percentage_fans_b = fans_b/number_of_all_fans * 100
percentage_fans_v = fans_v/number_of_all_fans * 100
percentage_fans_g = fans_g/number_of_all_fans * 100
percentage_all_fans_capacity = number_of_all_fans /capacity_of_the_stadium * 100


print(f"{percentage_fans_a:.2f}%")
print(f"{percentage_fans_b:.2f}%")
print(f"{percentage_fans_v:.2f}%")
print(f"{percentage_fans_g:.2f}%")
print(f"{percentage_all_fans_capacity:.2f}%")
