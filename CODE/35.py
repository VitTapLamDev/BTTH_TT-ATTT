import random

def is_prime(n, k=10):
    # n là số cần kiểm tra, k là số lần kiểm tra
    if n <= 1 or n == 4:
        return False
    if n <= 3:
        return True
    # Chuyển n thành d * 2^r
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    # Lặp qua k lần
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Nhập số nguyên n từ bàn phím
n = int(input("Nhập số nguyên n: "))

# Kiểm tra và in kết luận
if is_prime(n):
    print(f"{n} là số nguyên tố")
else:
    print(f"{n} không phải là số nguyên tố")
