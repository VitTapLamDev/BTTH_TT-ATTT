import math
import random 

def check_prime(n):
    check = True
    if n == 1: return False
    elif n == 2: return True
    else:
        for i in range(3, math.ceil(math.sqrt(n)) + 1):
            if n % i == 0:
                check = False
                break
    return check

def doi_nhi_phan(n):
    k = []
    while (n>0):
        a = int(float(n%2)) 
        k.append(a) 
        n = (n-a)/2
    k.reverse() 
    return k

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
    return y2

def cripsto(SBD):
    b, c, d, p, q, e = 1, 1, 1, 1, 1, 0
    while check_prime(q) is False and check_prime(p) is False:
        p = int(random.randrange(101, 500, 2))
        q = int(random.randrange(101, 500, 2))
    phi = (q-1)*(p-1)
    n = q * p
    m = SBD + 123
    for i in range(10000, phi):
        if math.gcd(phi, i) == 1:
            e = i
            break
    d = euclide_extended(phi, e)
    if d < 0: d = d + phi
    
    list_e = doi_nhi_phan(e)
    list_d = doi_nhi_phan(d)
    print(list_e)
    for i in range(len(list_e)):
        a = pow(c, 2, n)
        print(list_e[i], a, end="  ")
        if list_e[i] == 1: 
            c = (a * m) % n
            print(c)
        else: 
            c = a
            print(c)
    print("---------------------------------")
    print(list_d)
    for i in range(len(list_d)):
        a = pow(b, 2, n)
        print(list_d[i], a, end= "  ")
        if list_d[i] == 1: 
            b = (a * c) % n
            print(b)
        else: 
            b = a 
            print(b)
    print('p, q, phi, e, d, n = {0}, {1}, {2}, {3}, {4}, {5}'.format(p,q,phi,e,d,n))
    print('Ban ma: {0}'.format(c))
    print('Ban ro: {0}'.format(b -123))
    
def main():
    SBD = int(input('Nhap vao so bao danh: '))
    if SBD <= 0: 
        print('Wrong Inpur!')
    else: 
        cripsto(SBD)

main()