def fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def listfibo(n):
    for i in range(1, n + 1):
        print(fibonacci(i), end='\t')

# Gọi thử
print("Số Fibonacci thứ 9 là:", fibonacci(9))
print("Dãy Fibonacci từ 1 đến 9:")
listfibo(9)
