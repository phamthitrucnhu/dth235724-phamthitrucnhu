def ToiUuChuoiDanhTu(s):
    s = s.strip()  # bỏ khoảng trắng đầu và cuối
    words = s.split()  # tách các từ, tự loại bỏ khoảng trắng thừa
    result = ' '.join(word.capitalize() for word in words)  # Viết hoa chữ cái đầu
    return result

# Test chương trình
chuoi = "  TRần   duY     thAnH   "
print("Chuỗi ban đầu:", repr(chuoi))
chuoi_toi_uu = ToiUuChuoiDanhTu(chuoi)
print("Chuỗi tối ưu:", repr(chuoi_toi_uu))
