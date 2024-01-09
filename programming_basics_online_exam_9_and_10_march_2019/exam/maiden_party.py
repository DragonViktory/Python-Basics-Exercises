price_maiden_party = float(input())
amount_love_messages = int(input())
amount_wax_roses = int(input())
amount_key_chains = int(input())
amount_cartoons = int(input())
amount_luck_hit = int(input())

price_love_messages = amount_love_messages * 0.60
price_wax_roses = amount_wax_roses * 7.20
price_key_chains = amount_key_chains * 3.60
price_cartoons = amount_cartoons * 18.20
price_luck_hit = amount_luck_hit * 22

all_items = amount_love_messages + amount_wax_roses + amount_key_chains + amount_cartoons + amount_luck_hit
total_price_without_discount = price_love_messages + price_wax_roses + price_key_chains + price_cartoons + price_luck_hit

if all_items >= 25:
    discount = total_price_without_discount * 0.35
    total_price_whit_discount = total_price_without_discount - discount
    total_money_on_hand = total_price_whit_discount - (total_price_whit_discount * 0.10)
else:
    total_money_on_hand = total_price_without_discount - (total_price_without_discount * 0.10)
difference = abs(price_maiden_party - total_money_on_hand)
if total_money_on_hand >= price_maiden_party:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
