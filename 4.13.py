# Câu 13: Kiểm tra số hoàn thiện và số thịnh vượng

def uoc_so(n):
    """Trả về danh sách các ước số dương của n (không tính n)."""
    uoc = []
    for i in range(1, n):
        if n % i == 0:
            uoc.append(i)
    return uoc

def la_hoan_thien(n):
    """Kiểm tra n có phải số hoàn thiện không."""
    return sum(uoc_so(n)) == n

def la_thinh_vuong(n):
    """Kiểm tra n có phải số thịnh vượng không."""
    return sum(uoc_so(n)) > n

# Test câu 13
print("Kiểm tra số hoàn thiện:")
test_numbers = [6, 28, 12, 10, 496]
for num in test_numbers:
    print(f"{num}: {'Hoàn thiện' if la_hoan_thien(num) else 'Không hoàn thiện'}")

print("\nKiểm tra số thịnh vượng:")
test_numbers2 = [6, 12, 18, 20, 24]
for num in test_numbers2:
    print(f"{num}: {'Thịnh vượng' if la_thinh_vuong(num) else 'Không thịnh vượng'}")
