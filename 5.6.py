import re

def NegativeNumberInStrings(s):
    numbers = re.findall(r'-\d+', s)
    print("Các số nguyên âm trong chuỗi là:")
    for num in numbers:
        print(num)

# Ví dụ sử dụng
chuoi = "abc-5xyz-12k9l--p"
NegativeNumberInStrings(chuoi)
