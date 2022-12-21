def calcu(n):
    list_prime = []
    p = 0; q = 0; k = 0
    for i in range(1, n+1):
        if n % i == 0:
            list_prime.append(i)
            p += i
            
    s = len(list_prime)
    
    for i in range(1,s):
        check = True
        for j in range(2,list_prime[i]):
            if (list_prime[i] == 1) or (list_prime[i] % j == 0):
                check = False
                break   
        if check is True:
            q += list_prime[i]
            k += 1
            
    sum = n+p+s-q-k
    print('N + p + s - q - k = {0}'.format(sum))
            
def main():
    n = int(input('Nhap vao so nguyen duong N: '))
    calcu(n)

main()