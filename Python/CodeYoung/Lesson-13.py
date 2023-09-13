row = 3
col = 5

for i in range(0,row):
    for j in range (0,col):
        print("*",end="")
    print()


size = 5
for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print('*', end='')
        else:
            print(' ', end='')
    print()

for i in range(6):
    for j in range(1,i+1):
        print("*",end="")
    print()
    

for i in range(size):
    for j in range(size-i):
        print("*",end="")
    print() 