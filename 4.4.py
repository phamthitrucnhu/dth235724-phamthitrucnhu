def ROI(dt, cp):
    return (dt - cp) / cp

def GoiYDauTu(roi):
    if roi >= 0.75:
        return "Nên đầu tư"
    else:
        return "Không nên đầu tư"

# Giao diện nhập liệu
print("📈 Chương trình tính ROI (Return on Investment)")
try:
    dt = int(input("Nhập Doanh Thu: "))
    cp = int(input("Nhập Chi Phí: "))

    if cp == 0:
        print("❌ Lỗi: Chi phí không được bằng 0.")
    else:
        roi = ROI(dt, cp)
        print("🔢 Tỉ lệ ROI = {:.2f}".format(roi))
        print("💡 Gợi ý:", GoiYDauTu(roi))

except ValueError:
    print("❌ Lỗi: Vui lòng nhập số nguyên hợp lệ!")
