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

def find_super_num(n):
    for i in range(2, n):
        list = find_primes(i)
        for j in range(len(list)):
            if (i%list[j]==0) and (i%pow(list[j], 2)==0):
                print(i)
                break
        
def main():
    n = int(input('Nhap vao STN n < 10000: '))
    if 0 < n < 10000:
        find_super_num(n)
    else:
        print('Wrong Input!! Try Again!!')
    
if __name__ == '__main__':
    main()