number_visitors_fitness = int(input())
people_exercising_back = 0
people_exercising_chest = 0
people_exercising_legs = 0
people_exercising_abs = 0
people_who_bought_a_protein_shake = 0
people_who_bought_a_protein_bar = 0
total_visitors = 0

for _ in range(number_visitors_fitness):
    activity = input()
    if activity == "Back":
        people_exercising_back += 1
    elif activity == "Chest":
        people_exercising_chest += 1
    elif activity == "Legs":
        people_exercising_legs += 1
    elif activity == "Abs":
        people_exercising_abs += 1
    elif activity == "Protein shake":
        people_who_bought_a_protein_shake += 1
    elif activity == "Protein bar":
        people_who_bought_a_protein_bar += 1
total_visitors_work_out = people_exercising_back + people_exercising_chest + people_exercising_legs + people_exercising_abs
total_visitors_protein = people_who_bought_a_protein_shake + people_who_bought_a_protein_bar
percentage_work_out = total_visitors_work_out / number_visitors_fitness * 100
percentage_protein = total_visitors_protein/ number_visitors_fitness * 100

print(f"{people_exercising_back} - back")
print(f"{people_exercising_chest} - chest")
print(f"{people_exercising_legs} - legs")
print(f"{people_exercising_abs} - abs")
print(f"{people_who_bought_a_protein_shake} - protein shake")
print(f"{people_who_bought_a_protein_bar} - protein bar")
print(f"{percentage_work_out:.2f}% - work out")
print(f"{percentage_protein:.2f}% - protein")
