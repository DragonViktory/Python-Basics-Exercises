nylon = int(input())
paint = int(input())
paint_thinner = int(input())
hours = int(input())
bags = 0.40

sum_nylon = (nylon + 2) * 1.50
sum_paint = (paint + (paint * 0.10)) * 14.50
sum_paint_thinner = paint_thinner * 5.00
sum_materials = sum_nylon + sum_paint + sum_paint_thinner + bags
sum_one_hour_work = sum_materials  * 0.30
sum_of_all_costs = sum_materials + (hours * sum_one_hour_work)
print(f"{sum_of_all_costs}")
