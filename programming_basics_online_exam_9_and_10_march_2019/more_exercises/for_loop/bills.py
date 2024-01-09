months = int(input())
total_electricity_expenses = 0
total_water_expenses = 0
total_internet_expenses = 0
total_other_expenses = 0
total_expenses = 0

for expenses in range(months):
    electricity_expenses = float(input())
    total_electricity_expenses += electricity_expenses
    total_water_expenses += 20
    total_internet_expenses += 15
    total_other_expenses = (total_electricity_expenses + total_water_expenses + total_internet_expenses) * 0.2
total_expenses += total_electricity_expenses + total_water_expenses + total_internet_expenses + total_other_expenses
average_expenses = (total_electricity_expenses
                    + total_water_expenses
                    + total_internet_expenses
                    + total_expenses) / months

print(f"Electricity: {total_electricity_expenses:.2f} lv")
print(f"Water: {total_water_expenses:.2f} lv")
print(f"Internet: {total_internet_expenses:.2f} lv")
print(f"Other: {total_expenses:.2f} lv")
print(f"Average: {average_expenses:.2f} lv")
