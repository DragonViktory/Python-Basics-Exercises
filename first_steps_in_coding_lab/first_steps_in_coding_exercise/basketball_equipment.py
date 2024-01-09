free_basketball = int(input())

shoes_price = free_basketball - (free_basketball * 0.40)
clothes_price = shoes_price - (shoes_price * 0.20)
ball_price = clothes_price / 4
accessories = ball_price / 5

total_sum = free_basketball + shoes_price + clothes_price + ball_price + accessories
print(f"{total_sum:.2f}")
