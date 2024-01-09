rent = int(input())
statuettes = rent - (rent *0.30)
kettering = statuettes - (statuettes * 0.15)
voiceover = kettering /2

total_sum = rent + statuettes + kettering + voiceover

print(f"{total_sum:.2f}")