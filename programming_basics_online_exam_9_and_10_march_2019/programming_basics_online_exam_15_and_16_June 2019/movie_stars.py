budget = float(input())
command = input()
salary = 0
enough_budget = True

while command != "ACTION":
    if len(command) <= 15:
        salary = float(input())
    else:
        salary = budget * 20 / 100
    budget -= salary
    if budget <= 0:
        enough_budget = False
        break
    command = input()

if enough_budget:
    print(f"We are left with {budget:.2f} leva.")
else:
    difference = abs(budget)
    print(f"We need {difference:.2f} leva for our actors.")
