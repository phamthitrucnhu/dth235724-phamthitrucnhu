def CheckPrime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

s = "5;7;8;-2;8;11;-13;9;10"
arr = s.split(';')

sochan = 0
soam = 0
sont = 0
tong = 0  # tránh dùng tên biến là `sum` vì trùng hàm dựng sẵn

for x in arr:
    print(x)
    number = int(x)
    if number % 2 == 0:
        sochan += 1
    if number < 0:
        soam += 1
    if CheckPrime(number):
        sont += 1
    tong += number

print("Số chẵn =", sochan)
print("Số âm =", soam)
print("Số nguyên tố =", sont)
print("Trung bình =", tong / len(arr))
