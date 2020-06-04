'''
This function/program returns the number of occurnace of letters/numbers/special character
'''
import re
count = 0
count1 = 0
s='SHAMSunnisa1233445'

x=re.findall('[a-z]',s)
a=re.findall('[0-9]',s)
print(x)
print(a)
for i in x:
    x1=x.count(i)
    print(f'count {i} is {x1}')
for i in a:
    x2=a.count(i)
    print(f'count of {i} is {x2}')