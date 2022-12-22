import math

def check_prime(n):
    check = True
    if n == 1: return False
    elif n == 2: return True
    else:
        for i in range(2, math.ceil(math.sqrt(n)) + 1):
            if n % i == 0:
                check = False
                break
    return check

def main ():
    print('Ax^2 + Bx + c')
    a = int(input('Nhap vao so a: '))
    b = int(input('Nhap vao so b: '))
    c = int(input('Nhap vao so c: '))
    print('[m, l]')
    m = int(input('Nhap vao khoang m: '))
    l = int(input('Nhap vao khoang l: '))
    if (a%2==0) and (b%2==0) and (c%2==0):
        check = False
    else:
        for x in range(m, l+1):
            if check_prime(a*pow(x, 2) + b*x + c) is True:
                check = True
                print('x = {0}, mod = {1}'.format(x, a*pow(x, 2) + b*x + c ))
    if check is False:
        print("Khong co gia tri x thoa man")

if __name__ == '__main__':
    main()