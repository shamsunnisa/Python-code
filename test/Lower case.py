def char(val):
    s=""
    for i in val:
        if i.isupper():
            s=s+i.lower()
        #print(s)
        else:
             s=s+i.upper()
    print(s)


char('Hello')
