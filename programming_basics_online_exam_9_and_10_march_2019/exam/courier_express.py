shipment_weight_kg = float(input())
service_type = input()
distance_in_kilometers = int(input())
current_price = 0

if service_type == "standard":
    if shipment_weight_kg < 1:
        current_price = 0.03
    elif shipment_weight_kg < 10:
        current_price = 0.05
    elif shipment_weight_kg < 40:
        current_price = 0.10
    elif shipment_weight_kg < 90:
        current_price = 0.15
    else:  # shipment_weight_kg <= 150:
        current_price = 0.20
    total_price = current_price * distance_in_kilometers

elif service_type == "express":
    if shipment_weight_kg < 1:
        current_price = 0.03
        markup_per_kg = 0.03 * 0.80
        total_markup = shipment_weight_kg * markup_per_kg * distance_in_kilometers
    elif shipment_weight_kg < 10:
        current_price = 0.05
        markup_per_kg = 0.05 * 0.40
        total_markup = shipment_weight_kg * markup_per_kg * distance_in_kilometers
    elif shipment_weight_kg < 40:
        current_price = 0.10
        markup_per_kg = 0.10 * 0.05
        total_markup = shipment_weight_kg * markup_per_kg * distance_in_kilometers
    elif shipment_weight_kg < 90:
        current_price = 0.15
        markup_per_kg = 0.15 * 0.02
        total_markup = shipment_weight_kg * markup_per_kg * distance_in_kilometers
    else:  # shipment_weight_kg <= 150:
        current_price = 0.20
        markup_per_kg = 0.15 * 0.01
        total_markup = shipment_weight_kg * markup_per_kg * distance_in_kilometers
    total_price = (current_price * distance_in_kilometers) + total_markup
print(f"The delivery of your shipment with weight of {shipment_weight_kg:.3f} kg. would cost {total_price:.2f} lv.")
