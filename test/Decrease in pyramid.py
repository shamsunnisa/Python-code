def pyramid(val):
    s=0
    for i in range(val,0,-1):
        for j in range(i,0,-1):
            print(j,end="")
        print('\r')


pyramid(5)
