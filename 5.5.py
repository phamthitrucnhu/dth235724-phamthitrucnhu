def xu_ly_chuoi(s):
    in_hoa = 0
    in_thuong = 0
    chu_so = 0
    ky_tu_dac_biet = 0
    khoang_trang = 0
    nguyen_am = 0
    phu_am = 0

    for ch in s:
        if ch.isupper():
            in_hoa += 1
        elif ch.islower():
            in_thuong += 1
        elif ch.isdigit():
            chu_so += 1
        elif ch.isspace():
            khoang_trang += 1
        else:
            ky_tu_dac_biet += 1

        if ch.lower() in 'aeiou':
            nguyen_am += 1
        elif ch.isalpha():
            phu_am += 1

    print("Số chữ IN HOA:", in_hoa)
    print("Số chữ in thường:", in_thuong)
    print("Số chữ số:", chu_so)
    print("Số ký tự đặc biệt:", ky_tu_dac_biet)
    print("Số khoảng trắng:", khoang_trang)
    print("Số nguyên âm:", nguyen_am)
    print("Số phụ âm:", phu_am)

# Nhập và chạy chương trình
s = input("Nhập chuỗi: ")
xu_ly_chuoi(s)
