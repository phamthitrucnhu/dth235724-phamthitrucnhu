from random import randrange

# Danh sách giá trị cần kiểm tra
values_to_check = [4.5, 34, -1, 100, 0, 99]

# Hàm kiểm tra xem giá trị có thể xuất hiện trong randrange(0, 100) không
def check_randrange_values():
    valid_range = list(range(0, 100))  # Tập các giá trị có thể xuất hiện
    print("Kiểm tra các giá trị có thể xuất hiện trong randrange(0, 100):\n")
    for value in values_to_check:
        if isinstance(value, int) and value in valid_range:
            print(f"{value} ✅ Có thể xuất hiện")
        else:
            print(f"{value} ❌ Không thể xuất hiện")

check_randrange_values()
