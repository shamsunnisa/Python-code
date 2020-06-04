import os

class stacks():

    st = []

    def __init__(self):
        self.st = []

    def push(self):
        item = int(input('Enter the item -> '))
        self.st.append(item)

    def pop(self):
        if ( len(self.st) == 0):
            print('---- Stack is MT --- ')
        else:
            print('Popped item is -> ' , self.st.pop())

    def show(self):
        print('--- stack is ---')
        for i in self.st[::-1]:
            print(i)

s = stacks()

while(True):
  #  os.system('cls')
    print('\tMenu')
    print('\t 1. Push \n\t 2. Pop \n\t 3. Show \n\t 4. Exit')
    inp = int(input('Enter the choice -> '))
    if inp == 1:
        s.push()
    elif inp == 2:
        s.pop()
    elif inp == 3:
        s.show()
    else:
        print('End of the program')
        break









