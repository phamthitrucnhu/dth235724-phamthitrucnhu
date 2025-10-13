def doc_so(n):
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi",
                 "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

    if n < 0 or n > 99:
        return "Số không hợp lệ!"

    if n == 0:
        return "không"

    if n < 10:
        return don_vi[n]

    chuc = n // 10
    dv = n % 10

    result = hang_chuc[chuc]

    # Xử lý cách đọc đặc biệt ở hàng đơn vị
    if dv == 1 and chuc != 1:
        result += " mốt"
    elif dv == 5 and chuc != 0:
        result += " lăm"
    elif dv != 0:
        result += " " + don_vi[dv]

    return result.strip()


# Nhập số từ bàn phím
n = int(input("Nhập số nguyên n (0 - 99): "))
print("Cách đọc:", doc_so(n))
