import math

def count_prime(n):
    count = 0
    for i in range(2,n):
        check = True
        for j in range(2,math.ceil(i/2) + 1):
            if i % j == 0:
                check = False
                break
        if check is True:
            count += 1
    print('So so nguyen to nho hon {0} la: {1}'.format(n, count))
    
def main():
    n = int(input('Nhap vao so tu nhien: '))
    count_prime(n)
    
main()