count_of_pages = int(input())
pages_read_in_one_hour = int(input())
days = int(input())
hours = count_of_pages // pages_read_in_one_hour
needed_hours_per_day = hours // days
print(needed_hours_per_day)