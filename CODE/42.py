import math
import random

def check_prime(n):
    check = True
    if n <= 1: return False
    elif n == 2: return True
    else:
        for i in range(2, math.ceil(math.sqrt(n)) + 1):
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

def nhanBinhPhuong(a, k, n):
    list_k = doi_nhi_phan(k)
    p = 1 
    for i in range(len(list_k)):
        p = pow(p, 2, n)
        if list_k[i] == 1:
            p = (p * a) % n
    return p

def main():
    p, q, a, count = 1, 1, 1, 0
    while check_prime(q) is False and check_prime(p) is False:
        p = int(random.randrange(1, 1000, 2))
        q = int(random.randrange(1, 1000, 2))
    for a in range(1, 100):
        if check_prime(nhanBinhPhuong(a, p, q)) is True:
            count += 1
            print('{0}: {1}^{2} mod {3} = {4}'.format(count, a, p, q, nhanBinhPhuong(a, p, q)))
    print("So cap thoa man: " + str(count))
if __name__ == '__main__':
    main()