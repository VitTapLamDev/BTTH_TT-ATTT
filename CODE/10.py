import math

def check_prime(n):
    check = True
    if n <= 1: check = False
    if n == 2: check = True
    for i in range(2,math.ceil(math.sqrt(n)+1)):
        if n % i == 0:
            check = False
            break
    if check is True:
        return True
    
def find_quotient(n):
    count_quotient = 0 
    count_prime_quotient = 0
    for i in range(1, n+1):
        if n % i == 0:
            count_quotient += 1
            check_prime_quotient = check_prime(i)
            if check_prime_quotient is True:
                count_prime_quotient += 1
    print('So uoc cua {0} la: {1}'.format(n, count_quotient))
    print('So uoc nguyen to cua {0} la: {1}'.format(n, count_prime_quotient))

def main():
    n = int(input('Nhap vao so tu nhien: '))
    if n <= 0:
        print('Wrong Input!! Try again')
    else:
        find_quotient(n)
    
main()