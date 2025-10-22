import math

print("Nhập tọa độ điểm A:")
xA = float(input("xA = "))
yA = float(input("yA = "))

print("Nhập tọa độ điểm B:")
xB = float(input("xB = "))
yB = float(input("yB = "))

dAB = math.sqrt((xB - xA) ** 2 + (yB - yA) ** 2)

print("Độ dài đoạn AB =", round(dAB, 4))
