import math

m = 123456

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
    
def find_mod(id,n):
    print('{0}^{1} mod {2} = {3}'.format(id, n, m, (pow(id,n) % m))) 
    
def find_prime(n):
    ceil = 0; floor = 0; num = n + 1 
    for i in reversed(range(n)):
        if check_prime(i) is True:
            ceil = i
            break
    while floor == 0:
        if check_prime(num) is True:
            floor = num
            break
        else: num += 1
    print(floor, ceil)
    if (floor - n) < (n - ceil):
        find_mod(n, floor)
    else:
        find_mod(n, ceil)
             
def main():
    n = int(input('Nhap vao ma so sinh vien: '))
    if n < 0: print('Wrong Input!!')
    else: find_prime(n)        

main()