def sum_prime(a, b):
    num_a = a
    if a == 1:
        num_a = a + 1  
    sum = 0
    for i in range(num_a,b):
        check = True
        for j in range(2,i):
            if i % j == 0:
                check = False
                break
        if check is True:
            sum += i
    print('Tong cac so nguyen to trong khoang [{0}, {1}] la: {2}'.format(a, b, sum))
    
def main():
    print('Nhap vao khoang [a, b]:')
    a = int(input('Nhap vao so a: '))
    b = int(input('Nhap vao so b: '))
    if (a > 0) and (b > 0):
        sum_prime(a, b)
    else:
        print('Wrong Input! Try Again.')
        
main()
    
    