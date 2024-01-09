# i = 0
# while i <= 5:
#     print("SoftUni")
#     i += 1

# i = 0
# while i == 0:
#     print("SoftUni")
#     if i == 1:
#         break

# i = 0
# while i <= 6:
#     i += 1
#     if i % 2 == 0:
#         print(i, end="")
# 246

# i = 0
# while i < 5:
#     if i == 0:
#         print(i)
#         break
#     i += 1
# # 0

# for h in range(24):
#     for m in range(60):
#         print(f"{h}:{m}")

# for x in range(1, 11):
#     for y in range(1, 11):
#         product = x * y
#         print(f"{x} * {y} = {product}")


flag = False
for i in range(n):
    for j in range(n):
        if condition:
            flag = True
            break
    if flag:
        break
