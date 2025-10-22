import math

n = int(input("Nhập n (số lượng căn bậc 2 lồng nhau): "))
s = 0

for _ in range(n):
    s = math.sqrt(2 + s)

print(f"S({n}) = {round(s, 6)}")
