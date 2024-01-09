groups_of_climbers = int(input())
climbers_musala = 0
climbers_mont_blanc = 0
climbers_kilimanjaro = 0
climbers_k2 = 0
climbers_everest = 0
total_people = 0
for _ in range(groups_of_climbers):
    number_people = int(input())
    total_people += number_people
    if number_people <= 5:
        climbers_musala += number_people
    elif number_people <= 12:
        climbers_mont_blanc += number_people
    elif number_people <= 25:
        climbers_kilimanjaro += number_people
    elif number_people <= 40:
        climbers_k2 += number_people
    else:  # elif number_people >= 41:
        climbers_everest += number_people

percentage_musala = (climbers_musala / total_people) * 100
percentage_mont_blanc = (climbers_mont_blanc / total_people) * 100
percentage_kilimanjaro = (climbers_kilimanjaro / total_people) * 100
percentage_k2 = (climbers_k2 / total_people) * 100
percentage_everest = (climbers_everest / total_people) * 100

print(f"{percentage_musala:.2f}%")
print(f"{percentage_mont_blanc:.2f}%")
print(f"{percentage_kilimanjaro:.2f}%")
print(f"{percentage_k2:.2f}%")
print(f"{percentage_everest:.2f}%")
