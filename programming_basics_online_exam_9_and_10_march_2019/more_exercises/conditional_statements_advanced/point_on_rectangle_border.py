x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

# x1 < x2
# y1 < y2

if (x == x1 or x == x2) and (y1 <= y <= y2):
    print(f"Border")
elif (y == y1 or y == y2) and (x1 <= x <= x2):
    print(f"Border")
else:
    print(f"Inside / Outside")

