pool_volume_in_liters = int(input())
flow_rate_of_the_first_pipe_per_hour = int(input())
flow_rate_of_the_second_pipe_per_hour = int(input())
hours = float(input())

total_liters_first = hours * flow_rate_of_the_first_pipe_per_hour
total_liters_second = hours * flow_rate_of_the_second_pipe_per_hour
total_liters_first_and_second = total_liters_first + total_liters_second
percentages_first = (total_liters_first / total_liters_first_and_second) * 100
percentages_second = (total_liters_second / total_liters_first_and_second) * 100
percentages_first_and_second = (total_liters_first_and_second / pool_volume_in_liters) * 100
difference = pool_volume_in_liters - total_liters_first_and_second
if total_liters_first_and_second > pool_volume_in_liters:
    print(f"For {hours:.2f} hours the pool overflows with {abs(difference):.2f} liters.")
else:
    print(
        f"The pool is {percentages_first_and_second:.2f}% full. Pipe 1: {percentages_first:.2f}%."
        f" Pipe 2: {percentages_second:.2f}%.")