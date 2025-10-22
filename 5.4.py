print("=== Các hàm xử lý chuỗi quan trọng trong Python ===")

s = "  Hello Python 123! "

print("Chuỗi gốc:", repr(s))
print("strip():", repr(s.strip()))          # loại bỏ khoảng trắng đầu cuối
print("lower():", s.lower())                # chuyển về chữ thường
print("upper():", s.upper())                # chuyển về chữ hoa
print("title():", s.title())                # viết hoa chữ cái đầu mỗi từ
print("replace():", s.replace("Python", "World"))  # thay thế
print("split():", s.split())                # tách chuỗi thành list
print("join():", "-".join(["a", "b", "c"])) # nối chuỗi
print("count('l'):", s.count("l"))          # đếm số lần xuất hiện
print("find('P'):", s.find("P"))            # tìm vị trí đầu tiên
print("isalpha():", "abc".isalpha())        # chỉ toàn chữ cái
print("isdigit():", "123".isdigit())        # chỉ toàn số
print("isalnum():", "abc123".isalnum())     # chỉ chữ + số
print("startswith('H'):", s.strip().startswith("H"))
print("endswith('!'):", s.strip().endswith("!"))
