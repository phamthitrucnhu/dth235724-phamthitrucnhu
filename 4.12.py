# Câu 12: Hàm oscillate
def oscillate(start, end):
    for i in range(start, end):
        yield i
        yield -i

# Test câu 12
print("Kết quả câu 12:")
for n in oscillate(-3, 5):
    print(n, end=' ')
print("\n")


