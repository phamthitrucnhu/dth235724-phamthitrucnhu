cases = [
    ("(a)", 3, 5, 7),
    ("(b)", 3, 7, 5),
    ("(c)", 5, 3, 7),
    ("(d)", 5, 7, 3),
    ("(e)", 7, 3, 5),
    ("(f)", 7, 5, 3)
]

for label, i, j, k in cases:
    # Áp dụng logic
    if i < j:
        if j < k:
            i = j
        else:
            j = k
    else:
        if j > k:
            j = i
        else:
            i = k

    # In kết quả
    print(f"{label} i = {i}, j = {j}, k = {k}")
