def addition():
    n1 = int(input("ENTER NUMBER - "))
    n2 = int(input("ENTER NUMBER - "))
    r = n1 + n2
    print(f'ADDITION OF {n1} and {n2} IS {r}')

def subtraction(a,b):
    print(f'Subtraction of {a} and {b} IS {a-b}')


def multiplication():
    n1 = int(input('ENTER NUMBER - '))
    n2 = int(input('ENTER NUMBER - '))
    r = n1 * n2
    return r

def division(nr,dr):
    return nr // dr

# m = multiplication()
# print(m)

# subtraction(100,m)

d = division(100,20)
print(d)

print(division(10,3))

print(division(75,division(25,5)))

print(division(
                division(100,10), #10
                division(50,25)   #2
            )
    )