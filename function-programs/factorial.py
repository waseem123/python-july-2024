def factorial(num):
    f = 1
    for i in range(1,num+1):
        f = f * i
    return f

def evenodd(num):
    if num%2==0:
        return True
    else:
        return False
    
def divide(num):
    return num/10
    
print(factorial(5))
print(evenodd(3))

if(evenodd(10)):
    print('EVEN NUMBER')
else:
    print('ODD NUMBER')
    
if(evenodd(8)):
    print(f'Factorial of 8 is {factorial(8)}')
else:
    print(f'DIVISION IS {divide(8)}')