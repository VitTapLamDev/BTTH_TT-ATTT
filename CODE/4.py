def find_prime_in_range(a, b):
    num_a = a
    if a == 1:
        num_a = a + 1  
    count = 0
    for i in range(num_a,b):
        check = True
        for j in range(2,i):
            if i % j == 0:
                check = False
                break
        if check is True:
            count += 1 
    print('So nguyen to trong khoang [{0}, {1}] la: {2}'.format(a, b, count))
    
def main():
    print('Nhap vao khoang [a, b]:')
    a = int(input('Nhap vao so a: '))
    b = int(input('Nhap vao so b: '))
    if (a > 0) and (b > 0):
        find_prime_in_range(a, b)
    else:
        print('Wrong Input! Try Again.')
        
main()
    
    