print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. CHECK EVEN OR ODD")
choice = int(input("ENTER YOUR CHOICE - "))

match(choice):
    case 1:
        a = int(input("ENTER FIRST NUMBER  - "))
        b = int(input("ENTER SECOND NUMBER - "))
        print(a+b)
    case 2:
        a = int(input("ENTER FIRST NUMBER  - "))
        b = int(input("ENTER SECOND NUMBER - "))
        print(a-b)
    case 3:
        a = int(input("ENTER FIRST NUMBER  - "))
        b = int(input("ENTER SECOND NUMBER - "))
        print(a*b)

    case 4:
        num = int(input("ENTER A NUMBER - "))
        if num%2==0:
            print(f'{num} IS EVEN')
        else:
            print(f'{num} IS ODD')
    case _:
        print('YOU ENTERED A WRONG INPUT. PLEASE SELECT THE OPTION BETWEEN 1 TO 3')