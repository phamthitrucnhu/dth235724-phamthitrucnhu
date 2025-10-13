def la_nam_nhuan(nam):
    return (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0)

def tim_ngay_tiep_theo(ngay, thang, nam):
    # Số ngày trong các tháng
    so_ngay_thang = [0, 31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

    # Kiểm tra năm nhuận
    if la_nam_nhuan(nam):
        so_ngay_thang[2] = 29

    # Tăng ngày
    ngay += 1

    # Nếu quá số ngày trong tháng hiện tại
    if ngay > so_ngay_thang[thang]:
        ngay = 1
        thang += 1

        # Nếu quá tháng 12 thì sang năm mới
        if thang > 12:
            thang = 1
            nam += 1

    return ngay, thang, nam


# Nhập ngày tháng năm
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

# Tính ngày kế tiếp
ngay_moi, thang_moi, nam_moi = tim_ngay_tiep_theo(ngay, thang, nam)

# In kết quả
print(f"Ngày kế tiếp: {ngay_moi}/{thang_moi}/{nam_moi}")
