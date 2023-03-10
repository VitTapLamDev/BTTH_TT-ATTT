import math
import time
start_time = time.time()

def doi_nhi_phan(n):
    k = []
    while (n>0):
        a = int(float(n%2)) 
        k.append(a) 
        n = (n-a)/2
    k.reverse() 
    return k

def nhanBinhPhuong(n, k, mod):
    list_k = doi_nhi_phan(k)
    p, a  = 1, 1 
    for i in range(len(list_k)):
        a = pow(p, 2, mod)
        if list_k[i] == 1:
            p = (a * n) % mod
        else: 
            p = a
    return p

def is_carmichael(n):
    for i in range(2, math.ceil(n/2)+1):
        if n % i == 0 :
            for b in range(2, n):
                if (math.gcd(b, n) == 1):
                    if nhanBinhPhuong(b, n-1, n) != 1:   #Có thể dùng hàm pow(b ,n-1, n) cũng được
                        return False
            return True
    return False
              
def main():
    n = int(input('Nhap vao so n: '))
    count = 0
    if (n >= 0) and (n <= 10000):
        for i in range(1, n):
            if is_carmichael(i) is True: 
                count += 1
                print(i)
    else:
        print('Wrong input !!')   
    print('So so Carmichael co trong khoang la: ' + str(count))
    print("--- %s seconds ---" % (time.time() - start_time))     

if __name__ == '__main__':
    main()