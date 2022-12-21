def check_prime(n):
    check = True
    if n == 1 or n == 0: check = False
    else:
        for i in range(2, n):
            if n % i == 0:
                check = False
                break
    if check is True: return check
    
def find_primes(n):
    sum = 0; quotient = 0
    list_primes_num = []
    for i in range(n):
        if check_prime(i) is True:
            list_primes_num.append(i)
    for i in range(len(list_primes_num) - 1):
        for j in range(i, len(list_primes_num)):
            sum = list_primes_num[j] + list_primes_num[i]
            quotient = list_primes_num[j] - list_primes_num[i]
            if check_prime(sum) is True and check_prime(quotient) is True:
                print('Cap so nguyen to thoa man ({0}, {1})'.format(list_primes_num[i], list_primes_num[j]))
        
def main():
    n = int(input('Nhap vao so tu nhien n: '))
    if n <= 1:
        print('Wrong Input!')
    else:
        find_primes(n)
main()