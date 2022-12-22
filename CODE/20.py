import math

def euclide_extended(number_1, number_2):
    a = number_1; b = number_2
    if b == 0: return(a, 1, 0)
    x2 = 1; y1 = 1; x1 = 0; y2 = 0
    while b > 0:
        q = math.floor(a/b)
        r = a - q * b
        x = x2 - q * x1
        y = y2 - q * y1
        a = b; b = r
        x2 = x1; x1 = x
        y2 = y1; y1 = y
    return(a)

def main():
    print('Nhap vao khoang (m, n): ')
    m = int(input('m: '))
    n = int(input('n: '))
    d = int(input('Nhap vao gia tri d cho truoc: '))
    count = 0
    if (0<m<1000) and (0<n<1000) and (0<d<1000):
        for i in range(m, n):
            for j in range(i+1, n+1):
                if euclide_extended(j, i) == d:
                    print(i, j)
                    count += 1           
        print('So cap thoa man la: ' + str(count))
    else:
        print('Wrong Input!!')

if __name__ == '__main__':
    main()