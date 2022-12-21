import math

def sum_prime(n):
    sum = 0
    for i in range(2, n+1):
        check = True
        for j in range(2, math.ceil(math.sqrt(i)) + 1):
            if i % j == 0:
                check = False
                break
        if check is True:
            sum += i
    print("Tong cac uoc nguyen to cua {0} la: {1}".format(n, sum))
    
def main():
    n = int(input('Nhap vao so tu nhien n: '))
    
    if n <= 0:
        print('Wrong Input!')
    else:
        sum_prime(n)
    
main()