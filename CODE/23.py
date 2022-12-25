import math

def check_prime(n):
    if n <= 1: return False
    if n == 2: return True
    else:
        for i in range(2, math.ceil(math.sqrt(n) +1)):
            if n % i == 0:
                return False
    return True

def main():
    print('Nhap vao khoang [A, B]: ')
    a = int(input("Nhap vao gia tri A: "))
    b = int(input('Nhap vao gia tri B: '))
    sum = 0
    if a>0 and b>0 and b>a:
        for i in range(a, b+1):
            if check_prime(i) is True:
                sum += i
        if check_prime(sum) is True:
            print('YES: ' + str(sum))
        else:
            print('NO: ' + str(sum))
    else:
        print('Wrong Input!!! Try Again')

if __name__ == "__main__":
    main()