import math

def check_prime(n):
    if n <= 1: return False
    if n == 2: return True
    else:
        for i in range(2, math.ceil(math.sqrt(n) +1)):
            if n % i == 0:
                return False
    return True

def count_number_prime(number_a, number_b, S1, S2):
    S = []
    for i in S1:
        for j in S2:
            sum = i + j
            if sum >= number_a and sum <= number_b \
                    and check_prime(sum) and sum not in S:
                S.append(sum)
    return S

def main():
    number_a = int(input('Nhập số a = '))
    number_b = int(input(f'Nhập số b >= 'f'{number_a} = '))

    if number_b >= number_a:
        q = int(math.sqrt(number_b))
        S1 = [x * x for x in range(1, q + 1)]
        S2 = [x * x for x in range(1, q + 1)]
        result = count_number_prime(number_a, number_b, S1, S2)
        if len(result) > 0:
            print(result)
            print(f'Số lượng : {len(result)}')
        else:
            print('Không có giá trị nào')
    else:
        print('Thử Lại')
        
if __name__ == '__main__':
    main()