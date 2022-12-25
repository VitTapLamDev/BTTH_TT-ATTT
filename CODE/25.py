import math

def check_prime(n):
    if n <= 1: return False
    if n == 2: return True
    else:
        for i in range(2, math.ceil(math.sqrt(n) +1)):
            if n % i == 0:
                return False
    return True

def find_primes(n):
    list_prime = []
    for i in range(2, n):
        if check_prime(i) is True:
            list_prime.append(i)
    return list_prime

def find_num(n, m):
    for num in range(2, n):
        list = find_primes(num)
        

def main():
    print('Nhap vao 2 STN m va n: ')
    n = int(input('Nhap vao gia tri 1<=n<=10000: '))
    m = int(input("Nhap vao gia tri 2<m<=100: "))
    if 1<=n<=10000 and 2<m<=100 :
        find_num(n, m)
    else:
        print('Wrong Input!! Try again')
        
    
if __name__ == "__main__":
    main()