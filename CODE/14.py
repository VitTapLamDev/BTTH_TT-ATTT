def find_num_prime(n):
    list_prime = []
    for i in range(pow(10,n-1), (pow(10, n)-1)):
        check = True
        for j in range(2,i-1):
            if i % j == 0:
                check = False
                break
        if check is True:
            list_prime.append(i)
    return list_prime
    
def find_reverse_num(n):
    reverse_num = 0
    while n > 0:
        last_num = n % 10
        reverse_num = reverse_num * 10 + last_num
        n = n // 10
    return reverse_num

def find_num(n):
    list_prime = find_num_prime(n)
    for i in range(len(list_prime)):
        num = find_reverse_num(list_prime[i])
        for j in range(num):
            if pow(j, 3) == num:
                print(list_prime[i], num, j)
def main():       
    find_num(3)
main()