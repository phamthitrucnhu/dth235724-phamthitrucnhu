import os

def lay_ten_file_day_du(path):
    return os.path.basename(path)

def lay_ten_bai_hat(path):
    ten_file = os.path.basename(path)
    ten_bai_hat, _ = os.path.splitext(ten_file)
    return ten_bai_hat

# Test
duong_dan = "d:\\music\\muabui.mp3"
print("Đường dẫn:", duong_dan)
print("Tên file đầy đủ:", lay_ten_file_day_du(duong_dan))
print("Tên bài hát:", lay_ten_bai_hat(duong_dan))
