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

def main():
    n = int(input('Nhap vao So Tu Nhien n: '))
    if n <= 0:
        print('Wrong Input!! Try Again')
    else:
        for i in range(1, n):
            if check_prime(i) is True and check_prime(i+2) is True:
                print(i, i + 2)
                
if __name__ == '__main__':
    main()