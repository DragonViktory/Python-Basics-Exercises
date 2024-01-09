budget = float(input())
number_video_cards = int(input())
number_processors = int(input())
number_ram_memory = int(input())
sum_video_cards = number_video_cards * 250
sum_processors = number_processors * sum_video_cards * 0.35
sum_ram_memory = number_ram_memory * sum_video_cards * 0.10
total_sum = sum_video_cards + sum_processors + sum_ram_memory

if number_video_cards > number_processors:
    total_sum *= 0.85
difference = abs(budget - total_sum)
if budget >= total_sum:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
