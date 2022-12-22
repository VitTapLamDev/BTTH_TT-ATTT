import math
import random

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
    n = int(input('Nhap vao kich thuoc cua mang: '))
    arr, arr_primes = [], []
    for i in range(n):
        a = random.randint(0, 10000)
        arr.append(a)
        if check_prime(a) is True:
            arr_primes.append(a)
    print('Mang sinh la: '+str(arr))
    if len(arr_primes) == 0:
        print('Khong co so nguyen to trong mang')
    else: 
        print('Cac so nguyen to trong mang: ' + str(arr_primes))
    
if __name__ =='__main__':
    main()
