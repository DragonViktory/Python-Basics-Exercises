import math
from math import ceil

people_count = int(input())
tax_enter = float(input())
price_one_sunbed = float(input())
price_one_umbrella = float(input())

total_sum_enter = people_count * tax_enter
people_count_sunbed = math.ceil(people_count * 0.75)
total_sum_sunbed = people_count_sunbed * price_one_sunbed
people_count_umbrella = math.ceil(people_count / 2)
total_sum_umbrella = people_count_umbrella * price_one_umbrella
total_sum = total_sum_enter + total_sum_sunbed + total_sum_umbrella

print(f"{total_sum:.2f} lv.")
