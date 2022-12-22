import math

def check_prime(n):
    check = True
    if n <= 1: check = False
    if n == 2: check = True
    else:
        for i in range (2, math.ceil(math.sqrt(n)) + 1):
            if (n % i == 0): 
                check = False 
                break
    if check is True:
        return check  

def find_sum(n):
    sum = 0 
    list_prime = []
    for i in range(2, n+1):
        num_prime = check_prime(i)
        if num_prime is True:
            list_prime.append(i)
    print(list_prime)
    for i in range(len(list_prime)-3):
        sum = list_prime[i] + list_prime[i+1] + list_prime[i+2] + list_prime[i+3]
        check_sum = check_prime(sum)
        if check_sum is True and sum < n:     
            print(list_prime[i], list_prime[i+1], list_prime[i+2], list_prime[i+3], end=" ")

def main():
    n = int(input('Nhap vao so tu nhien n: '))
    if n <= 1:
        print('Wrong Input!')
    else:
        find_sum(n)
        print(check_prime(170755))
main()