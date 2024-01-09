budget = float(input())
extras = float(input())
cost_clothing = float(input())

decor = budget * 0.10
total_sum_clothing = extras * cost_clothing

if extras >= 150:
    discount_cost_clothing = total_sum_clothing * 0.10
    total_sum_clothing -= discount_cost_clothing
costs_all = total_sum_clothing + decor
diff = abs(budget - costs_all)

if costs_all <= budget:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
