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

def  gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def main():
    list_num = []
    count = 0
    n = int(input('Nhap vao so phan tu cua mang: '))
    for i in range(n):
        if n > 0:
            a = int(input("Nhap vao phan tu thu {0}: ".format(i+1)))
            list_num.append(a)
        else:
            print("Gia tri phai > 0")
    print(list_num)
    
    for i in range(len(list_num)):
        for j in range(i+1, len(list_num)-1):
            if check_prime(gcd(list_num[i],list_num[j])) is True:
                print(list_num[i], list_num[j], gcd(list_num[i],list_num[j]))
                count += 1
                
    print('So cap thoa man: {0}'.format(count))  
    
main()