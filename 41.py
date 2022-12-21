import math

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

def nhanBinhPhuong(a, k, n):
    list_k = doi_nhi_phan(k)
    p = 1 
    for i in range(len(list_k)):
        p = pow(p, 2, n)
        if list_k[i] == 1:
            p = (p * a) % n
    return p

def main():
    a = int(input('Nhap vao so tu nhien a: '))
    k = int(input('Nhap vao so mu: '))
    n = int(input('Nhap vao so mod: '))
    if  (0 < a < 1000) and (0 < k < 1000) and (0 < n < 1000):
        if check_prime(nhanBinhPhuong(a, k, n)) is True:
            print('La So Nguyen To')
        else:
            print('La Hop so')
    else: 
        print('Wrong Input!!')
        
if __name__ == '__main__' :
    main()
