import math


def check_prime(n):
    if n <= 1: return False
    if n == 2: return True
    else:
        for i in range(2, math.ceil(math.sqrt(n) +1)):
            if n % i == 0:
                return False
    return True

def check_f(n):
    if n <= 2 :
        return n
    elif check_prime(n) is True:
        return n
    else:
        return 0

def main():
    print('Nhap vao khoang [L, R]: ')
    l = int(input("Nhap vao gia tri L: "))
    r = int(input('Nhap vao gia tri R: '))
    sum = 0
    if 0<l<=10000 and 0<=r<=10000 and r>l:
        for i in range(l, r):
            for j in range(i+1, r+1):
                sum += check_f(i) * check_f(j)
    else:
        print('Wrong Input!!! Try Again')
    print('Tổng F(i)*F(j) với j > i: ' + str(sum))     

if __name__ == "__main__":
    main()