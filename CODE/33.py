def extend_euclid(a, b, n):
    # Kiểm tra điều kiện dừng
    if b == 0:
        return (1, 0, a)
    x, y, d = extend_euclid(b, a % b, n)
    x, y = y, (x - (a // b) * y) % n
    return (x, y, d)

def inverse(a, n):
    x, y, d = extend_euclid(a, n, n)
    if d > 1:
        return None
    return x % n

def main():
    # Sử dụng g(x) = x^3 + x + 1 trên trường hữu hạn GF(2^3)
    g = [1, 1, 0, 1]
    n = len(g) - 1
    # Tìm đa thức nghịch đảo của g(x)
    inverse_g = inverse(g[0], 2**n)
    print("Đa thức nghịch đảo của g(x) là:")
    print(inverse_g)

if __name__ == "__main__":
    main()
