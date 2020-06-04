def eliminate(val):
    s=[]
    for i in val:
        if i not in s:
            s.append(i)
            print(s)

eliminate(['one','Two','Three','One','Two'])