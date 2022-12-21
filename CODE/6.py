import math
import time
start_time = time.time()

def find_divide(n):
    sum = 0
    list_divide = []
    for i in range(1, math.ceil(n/2)+1):
        if n % i == 0:
            list_divide.append(i)
            sum += i

    return sum
       
def find_rel_num(n):
    for i in range(1, n):
        sum_1 = find_divide(i)
        for j in range(i+1, n):
            sum_2 = find_divide(j)
            if sum_1 == j  and sum_2 == i :
                print('Cap so than thiet la: ({0}, {1})'.format(i,j) )

def main():
    n = int(input('Nhap vao so tu nhien n: ')) 
    if n < 0:
        print('Wrong Input!! Try Again')
    else:
       find_rel_num(n)
    print("--- %s seconds ---" % (time.time() - start_time))
main() 