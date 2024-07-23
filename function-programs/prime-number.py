def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True 

if isPrime(15):
    print("PRIME NUMBER")
else:
    print("NOT PRIME")