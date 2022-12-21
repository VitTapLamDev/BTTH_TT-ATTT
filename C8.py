import math

def t_prime(n):
    list_t_prime = []
    for i in range(1,n):     
        count = 2
        for j in range (2, math.ceil(i/2)+1):
            if (i % j == 0):
                count += 1
        if count == 3:
            list_t_prime.append(i)       
    print(list_t_prime)
def main():
    n = int(input('Nhap vao so n: '))
    t_prime(n)
    
main()
