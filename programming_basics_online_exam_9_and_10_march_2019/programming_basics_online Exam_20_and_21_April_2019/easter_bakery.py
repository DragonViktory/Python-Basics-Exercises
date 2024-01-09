price_one_kg_flour = float(input())
kg_flour = float(input())
kg_sugar = float(input())
number_eggs_shells = int(input())
yeast_packets = int(input())

price_one_kg_sugar = price_one_kg_flour * 0.75
price_eggs_shells = price_one_kg_flour * 1.10
price_yeast_packet = price_one_kg_sugar * 0.20

total_sum = price_one_kg_flour * kg_flour\
            + kg_sugar * price_one_kg_sugar \
            + number_eggs_shells * price_eggs_shells \
            + yeast_packets * price_yeast_packet
print(f"{total_sum:.2f}")