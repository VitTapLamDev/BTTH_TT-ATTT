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
    
def euclide_extended(number_1, number_2):
    a = number_1; b = number_2
    if b == 0: return(a, 1, 0)
    x2 = 1; y1 = 1; x1 = 0; y2 = 0
    while b > 0:
        q = math.floor(a/b)
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1
        a = b; b = r
        x2 = x1; x1 = x
        y2 = y1; y1 = y
    d = a; x= x2; y = y2
    return d

def find_num_prime(n):
    count = 0
    for i in range(2,n):
        for j in range(i, n):
            ucln = euclide_extended(j, i)
            check_ucln = check_prime(ucln)
            if check_ucln is True : 
                count += 1
            j -= 1
    print('So cap so thoa man UCLN la SNT trong khoang(0, 1000) la: {0} cap so'.format(count))
    
def main():
    find_num_prime(1000)     
main()