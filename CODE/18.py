import math
    
W = 8
p = 2147483647
m = math.ceil(math.log2(p))
t = math.ceil(m/W)

def solve(a, W):
	result = []
	n = []
	for i in range(t):
		n.append(pow(2, i*W))
	for i in n[::-1]:
		result.append(a//i)
		a = a%i
	return result

def solve_plus(a,b,W,t):
    epsilon = 0
    c = []
    for i in range(t):
        tong = a[i] + b[i] + epsilon
        if tong < 0 or tong > pow(2, W):
            epsilon = 1
        else:
            epsilon = 0
        tong = tong % pow(2,W)
        c.append(tong)
    print(epsilon, c[::-1])
        
       
def main():
    num_1 = int(input('Nhap vao so thu nhat: '))
    num_2 = int(input('Nhap vao so thu hai: '))
    a = solve(num_1, W)
    b = solve(num_2, W)
    a.reverse(); b.reverse()
    print('Thuat toan cong: ', end='')
    solve_plus(a, b, W, t, )
    print('{0} + {1} = {2}'.format(num_1, num_2,num_1 + num_2))
main()