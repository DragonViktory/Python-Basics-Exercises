budget = float(input())
destination = input()
season = input()
number_of_days = int(input())

if destination == "Dubai":
    if season == "Winter":
        action_day_price = 45000
    elif season == "Summer":
        action_day_price = 40000
elif destination == "Sofia":
    if season == "Winter":
        action_day_price = 17000
    elif season == "Summer":
        action_day_price = 12500
elif destination == "London":
    if season == "Winter":
        action_day_price = 24000
    elif season == "Summer":
        action_day_price = 20250
total_costs = number_of_days * action_day_price

if destination == "Dubai":
    total_costs = total_costs - (total_costs * 0.30)
elif destination == "Sofia":
    total_costs = total_costs + (total_costs * 0.25)
difference = abs(budget - total_costs)
if budget >= total_costs:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")


