processor_price_dollars = float(input())
video_card_price_dollars = float(input())
ram_memory_dollars = float(input())
number_ram_memories = int(input())
percentage_discount = float(input())

processor_price_leva = processor_price_dollars * 1.57
video_card_price_leva = video_card_price_dollars * 1.57
ram_memory_leva = ram_memory_dollars * 1.57

price_ram = number_ram_memories * ram_memory_leva
video_card_price_whit_discount = video_card_price_leva- (video_card_price_leva * percentage_discount)
processor_leva_whit_discount = processor_price_leva - (processor_price_leva * percentage_discount)

total_price = price_ram + video_card_price_whit_discount + processor_leva_whit_discount

print(f"Money needed - {total_price:.2f} leva.")
