count_bread = int(input())
count_eggs = int(input())
count_cookies = int(input())

price_bread = count_bread * 3.20
price_eggs = count_eggs * 4.35
price_cookies = count_cookies * 5.40
paint_for_eggs = count_eggs * 12 * 0.15

total_price = price_bread + price_eggs + price_cookies + paint_for_eggs
print(f"{total_price:.2f}")