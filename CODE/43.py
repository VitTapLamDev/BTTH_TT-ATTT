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
    n = int(input('Nhap vao so tu nhien n: '))
    p, count = 1, 0
    while check_prime(p) is False:
        p = random.randrange(1, 1000, 2)
    if (n>0) and (n<1000):
        for i in range(n):
            if check_prime(nhanBinhPhuong(i, p, n)) is True:
                count += 1
                print('{0}: {1}^{2} mod {3} = {4}'.format(count,i,p,n,nhanBinhPhuong(i, p, n)))
    else:
        print("Wrong Input!!")
                
if __name__ == '__main__':
    main()