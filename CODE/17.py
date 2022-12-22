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
    check = False
    for x in range(1, 100000):
        if check_prime(a*pow(x, 2) + b*x + c) is True:
            check = True
            print('{0}x^2 + {1}x + {2} = {3}'.format(a,b,c,a*pow(x, 2) + b*x + c))
            print('x = {0}'.format(x))
            break
    if check is False:
        print("Khong co gia tri x thoa man")

if __name__ == '__main__':
    main()