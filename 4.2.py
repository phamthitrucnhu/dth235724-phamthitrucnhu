from random import randrange

while True:
    somay = randrange(1, 101)  # Số ngẫu nhiên từ 1 đến 100
    solandoan = 0
    win = False

    while solandoan < 7:
        solandoan += 1
        try:
            songuoi = int(input(f"Máy đã chọn số từ [1..100], mời bạn đoán lần {solandoan}: "))
        except ValueError:
            print("Vui lòng nhập một số nguyên!")
            solandoan -= 1  # Không tính lần đoán sai định dạng
            continue

        if songuoi == somay:
            print("🎉 Chúc mừng bạn đoán đúng! Số máy là:", somay)
            win = True
            break
        elif songuoi < somay:
            print("Bạn đoán sai! 👉 Số máy lớn hơn.")
        else:
            print("Bạn đoán sai! 👉 Số máy nhỏ hơn.")

    if not win:
        print("💀 GAME OVER! Bạn đã hết lượt đoán. Số máy là:", somay)

    hoi = input("Bạn có muốn chơi tiếp không? (c: có / k: không): ").strip().lower()
    if hoi == "k":
        break

print("Cảm ơn bạn đã chơi game! Hẹn gặp lại 😊")
