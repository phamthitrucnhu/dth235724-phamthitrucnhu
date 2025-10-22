from random import randrange

print("Chương trình xử lý List")

n = int(input("Nhập số phần tử: "))
lst = [0] * n

# Tạo list ngẫu nhiên
for i in range(n):
    lst[i] = randrange(-100, 100)

print("List ngẫu nhiên là:")
print(lst)

# Thêm phần tử mới
print("Mời bạn thêm số mới:")
value = int(input())
lst.append(value)
print("List sau khi thêm:", lst)

# Đếm số xuất hiện
print("Bạn muốn đếm số nào:")
k = int(input())
dem = lst.count(k)
print(k, "xuất hiện", dem, "lần trong list")

# Hàm kiểm tra số nguyên tố
def CheckPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Đếm và tính tổng số nguyên tố
demnt = 0
tongnt = 0
for x in lst:
    if CheckPrime(x):
        demnt += 1
        tongnt += x

print("Có", demnt, "số nguyên tố trong list")
print("Tổng các số nguyên tố =", tongnt)

# Sắp xếp list
lst.sort()
print("List sau khi sort:")
print(lst)

# Xóa list
del lst
print("List sau khi xóa:")
print(lst if 'lst' in locals() else "List không còn tồn tại!")
