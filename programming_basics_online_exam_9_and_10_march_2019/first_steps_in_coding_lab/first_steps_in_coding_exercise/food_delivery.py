count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegetarian_menu = int(input())

amount_menus = count_chicken_menu * 10.35 + count_fish_menu * 12.40 + count_vegetarian_menu * 8.15
dessert = amount_menus * 0.20
delivery = 2.50
total_sum = amount_menus + dessert + delivery
print(f"{total_sum:.2f}")
