import random 

def nhanBinhPhuongCoLap(a,k,n):
    b = 1
    if k == 0:
        return b
    A = a
    if k & 1 == 1:
        b = a 
    for i in range (1, len(bin(k))-2): 
        A = pow(A, 2, n)
        if (k >> i) & 1 == 1:
            b = pow(A, b, n)
    return b 

def Fermat(n,t):
    for i in range(1, t+1):
        a = random.randint(2, n-2)
        r = nhanBinhPhuongCoLap(a, n-1, n)
        if r != 1:
            return 'Hop so'
    return 'Nguyen to'

def main():
    n = int(input('Nhap vao so tu nhien n: '))
    t = int(input('Nhap va so lan lap t: '))
    print(n, "->", Fermat(n,t))

if __name__ == "__main__":
    main()

