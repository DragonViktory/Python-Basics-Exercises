number_chrysanthemums = int(input())
number_roses = int(input())
number_tulips = int(input())
season = input()
holly_day = input()

if season == "Spring" or season == "Summer":
    price_chrysanthemums = 2.00
    price_roses = 4.10
    price_tulips = 2.50

elif season == "Autumn" or season == "Winter":
    price_chrysanthemums = 3.75
    price_roses = 4.50
    price_tulips = 4.15

number_of_flowers = number_chrysanthemums + number_roses + number_tulips
price_bouquet = number_chrysanthemums * price_chrysanthemums + number_roses * price_roses + number_tulips * price_tulips

if holly_day == "Y":
    price_bouquet = price_bouquet + (price_bouquet * 0.15)
if number_tulips >= 7 and season == "Spring":
    price_bouquet *= 0.95
if number_roses >= 10 and season == "Winter":
    price_bouquet *= 0.90
if number_of_flowers > 20:
    price_bouquet *= 0.80
price_bouquet += 2
print(f"{price_bouquet:.2f}")
