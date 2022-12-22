import math

def check_prime(n):
    check = True
    if n <= 1: check = False
    if n == 2: check = True
    else:
        for i in range(2, math.ceil(math.sqrt(n) +1)):
            if n % i == 0:
                check = False
                break
    return check

def find_super_primes(a, b):
    count_super_prime = 0
    for i in range(a, b+1):
        count_prime = 0
        if check_prime(i) is True:
            for j in range(2, i):
                if check_prime(j) is True:
                    count_prime += 1
            if check_prime(count_prime) is True:
                print('So so nguyen to < {0}: {1}'.format(i, count_prime))
                count_super_prime += 1
    print('So so sieu nguyen to: ' + str(count_super_prime))
                
def main():
    print('Nhap vao khoang [a, b]')
    a = int(input('a: '))
    b = int(input('b: '))
    if a>0 and b>0:
        find_super_primes(a, b)
    else:
        print('Wrong Input!!')
        
if __name__ == '__main__':
    main()