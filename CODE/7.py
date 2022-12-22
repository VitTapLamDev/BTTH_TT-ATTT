import math
import time
start_time = time.time()

def find_prime(n):
    check = True
    if n <= 1: check = False
    if n == 2: check = True
    for i in range (2, math.ceil(math.sqrt(n))):
        if (n % i == 0):
            check = False
            break
    if check is True:
        return check    

def find_reverse_num(n):
    reverse_num = 0
    while n > 0:
        last_num = n % 10
        reverse_num = reverse_num * 10 + last_num
        n = n // 10
    return reverse_num

def find_emirp(n):
    list_emirp = []
    for i in range(12, n):
        check_prime = find_prime(i)
        if check_prime is True:
            reverse_num = find_reverse_num(i)
            check_emirp = find_prime(reverse_num)
            if check_emirp is True:
                list_emirp.append(i)
    if len(list_emirp) == 0:
        print("No emirp in range!!")
    else:
        print(list_emirp)

def main():
    n = int(input('Nhap vao so tu nhien n: '))
    if n < 10:
        print('Wrong Input! Try Agian')
    else:
        find_emirp(n)
    
    print("--- %s seconds ---" % (time.time() - start_time))
main()