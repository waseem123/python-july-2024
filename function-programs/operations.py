def factorial():
    num = int(input("ENTER A NUMBER - "))
    f = 1
    for i in range(1,num+1):
        f = f * i
    print(f'Factorial of {num} IS {f}')

def evenodd(num):
    if num%2==0:
        print(f'{num} is EVEN')
    else:
        print(f'{num} is ODD')
    
def divide(num):
    return num/10


print("1. FACTORIAL")
print("2. CHECK EVEN OR ODD")
print("3. DIVIDE BY 10")
choice = int(input("ENTER YOUR CHOICE - "))

match choice:
    case 1:
        factorial()
    case 2:
        n = int(input("ENTER A NUMBER - "))
        evenodd(n)
    case 3:
        n = int(input("ENTER A NUMBER - "))
        print(f'DIVISION of {n} IS {divide(n)}')
    case _:
        print("WRONG INPUT.")