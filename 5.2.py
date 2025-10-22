def ToiUuChuoi(s):
    s2 = s.strip()  # loại bỏ khoảng trắng đầu cuối
    arr = s2.split(' ')  # tách chuỗi thành list theo dấu cách
    s2 = ""
    for x in arr:
        word = x
        if len(word.strip()) != 0:
            s2 = s2 + word + " "
    return s2.strip()

s = " Trần Duy Thanh "
print(s, "=>", len(s))
s = ToiUuChuoi(s)
print(s, "=>", len(s))
