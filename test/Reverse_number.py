def rev_num(num):
    rev=0
    while(num!=0):
        num1=num%10
        rev=rev*10+num1
        num=num//10
    print(f'reverse of number {rev}')


rev_num(321)

