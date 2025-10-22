from random import randrange

# Tạo ma trận ngẫu nhiên m dòng, n cột
def TaoMaTran(m, n):
    D = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randrange(100))  # giá trị từ 0 đến 99
        D.append(row)
    return D

# Xuất ma trận
def XuatMaTran(D):
    print("Ma trận vừa tạo là:")
    for row in D:
        for element in row:
            print(element, end='\t')
        print()

# Trích dòng r
def LayDong(D, r):
    if 0 <= r < len(D):
        return D[r]
    else:
        print("Dòng không hợp lệ!")
        return []

# Trích cột c
def LayCot(D, c):
    C = []
    if 0 <= c < len(D[0]):
        for i in range(len(D)):
            C.append(D[i][c])
    else:
        print("Cột không hợp lệ!")
    return C

# Xuất 1 list 1 chiều
def XuatList1Chieu(R):
    for element in R:
        print(element, end='\t')
    print()

# Tìm số lớn nhất trong ma trận
def MAX(D):
    max_val = D[0][0]
    for row in D:
        for element in row:
            if element > max_val:
                max_val = element
    return max_val

# === CHƯƠNG TRÌNH CHÍNH ===
print("Nhập số dòng:")
m = int(input())
print("Nhập số cột:")
n = int(input())

D = TaoMaTran(m, n)
XuatMaTran(D)

print("Mời bạn nhập dòng muốn xuất (0 ->", m - 1, "):")
r = int(input())
dong = LayDong(D, r)
print("Dòng", r, "là:")
XuatList1Chieu(dong)

print("Mời bạn nhập cột muốn xuất (0 ->", n - 1, "):")
c = int(input())
cot = LayCot(D, c)
print("Cột", c, "là:")
XuatList1Chieu(cot)

print("Số lớn nhất trong ma trận =", MAX(D))
