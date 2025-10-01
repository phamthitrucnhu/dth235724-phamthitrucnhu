#Câu 6: Trình bày ý nghĩa toán tử /, //, %, **, and, or, is

#/ (chia thực): Thực hiện phép chia và trả về kết quả là số thực.
#Ví dụ: 5 / 2 = 2.5

#// (chia nguyên): Thực hiện phép chia và chỉ lấy phần nguyên.
#Ví dụ: 5 // 2 = 2

#% (chia lấy dư): Lấy phần dư trong phép chia.
#Ví dụ: 5 % 2 = 1

#** (lũy thừa): Tính lũy thừa của một số.
#Ví dụ: 2 ** 3 = 8 (tức là 2 mũ 3)

#and (và): Toán tử logic, trả về True nếu cả hai biểu thức đều đúng.
#Ví dụ: True and False = False

#or (hoặc): Toán tử logic, trả về True nếu ít nhất một biểu thức đúng.
#Ví dụ: True or False = True

#is: So sánh hai biến có cùng trỏ đến một đối tượng trong bộ nhớ hay không.
#Câu 7: Trình bày một số cách nhập dữ liệu từ bàn phím

#Sử dụng hàm input()
#Đây là cách phổ biến để nhập dữ liệu từ người dùng:

#name = input("Nhập tên của bạn: ")
#print("Xin chào", name)


#Ép kiểu khi nhập số
#Dữ liệu nhập vào luôn là chuỗi, nên cần chuyển đổi kiểu nếu cần:

#age = int(input("Nhập tuổi của bạn: "))


#Nhập nhiều giá trị một lúc
#Dùng split() và map() để chia và chuyển đổi:

#a, b = map(int, input("Nhập hai số cách nhau bằng dấu cách: ").split())

#Câu 8: Trình bày các loại lỗi khi lập trình và cách bắt lỗi trong Python

#Một số loại lỗi thường gặp:

#SyntaxError: Sai cú pháp.
#Ví dụ: if x = 5: (thiếu dấu ==)

#NameError: Gọi một biến chưa được khai báo.
#Ví dụ: print(x) khi chưa khai báo x

#TypeError: Thực hiện phép toán không hợp lệ giữa các kiểu dữ liệu.
#Ví dụ: "2" + 3 (chuỗi + số)

#ValueError: Ép kiểu dữ liệu không phù hợp.
#Ví dụ: int("abc")

#IndexError: Truy cập vị trí ngoài phạm vi của danh sách.
#Ví dụ: a = [1, 2]; a[5]

#ZeroDivisionError: Chia cho 0.
#Ví dụ: 10 / 0

#Cách bắt lỗi trong Python: Dùng try...except:

#try:
  #  x = int(input("Nhập một số: "))
 #   result = 10 / x
#except ZeroDivisionError:
 #   print("Không được chia cho 0.")
#except ValueError:
 #   print("Vui lòng nhập một số hợp lệ.")
#else:
 #   print("Kết quả là:", result)
#finally:
 #   print("Chương trình kết thúc.")

#try: Đoạn mã có thể gây lỗi

#except: Bắt và xử lý lỗi cụ thể

#else: Chạy nếu không có lỗi

#finally: Luôn chạy, dù có lỗi hay không