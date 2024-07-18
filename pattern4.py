for i in range(1,6):
    for j in range(1,6):
        if j>(5-i):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print("_--------------------_")
for i in range(1,16):
    for j in range(1,16):
        if j>(15-i):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    for k in range(1,i):
        print('*',end=' ')
    print()