count_group = int(input())

group_musala = 0
group_mont_blanc = 0
group_kilimanjaro = 0
group_k2 = 0
group_everest = 0
total_participants = 0

for _ in range(1, count_group + 1):
    participants = int(input())
    total_participants += participants
    if participants <= 5:
        group_musala += participants

    elif participants <= 12:
        group_mont_blanc += participants

    elif participants <= 25:
        group_kilimanjaro += participants

    elif participants <= 40:
        group_k2 += participants

    elif participants >= 41:
        group_everest += participants

percent_group_musala = group_musala / total_participants * 100
print(f"{percent_group_musala:.2f}%")
percent_group_mont_blanc = group_mont_blanc / total_participants * 100
print(f"{percent_group_mont_blanc:.2f}%")
percent_group_kilimanjaro = group_kilimanjaro / total_participants * 100
print(f"{percent_group_kilimanjaro:.2f}%")
percent_group_k2 = group_k2 / total_participants * 100
print(f"{percent_group_k2:.2f}%")
percent_group_everest = group_everest / total_participants * 100
print(f"{percent_group_everest:.2f}%")
