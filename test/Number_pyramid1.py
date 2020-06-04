def pyramid(val):
    s=0
    for i in range(1,val):
        for j in range(1,i+1):
            print(j,end="")
        print('\r')


pyramid(5)
