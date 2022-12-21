def find_num(n):
    list_prime = []
    for i in range(pow(10,n-1), (pow(10, n)-1)):
        check = True
        for j in range(2,i-1):
            if i % j == 0:
                check = False
                break
        if check is True:
            list_prime.append(i)
    print(list_prime)
    
def main():
    count_num = int(input("Nhap vao so chu so: "))
    if (count_num >= 2) and (count_num <= 10):
        find_num(count_num)
    else:
        print("Wrong Input!! Try Agian")
    
main()