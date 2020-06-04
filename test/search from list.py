def search(ls):
    val = int ( input('Enter the number for search -> '))

    flag = False
    found = 0

    for i in ls:
        if i == val:
            flag = True
            found=i
    if flag:
        print('Found at ',found)
    else:
        print('Not Found')

search([1,2,3,4,5,6,7,8])