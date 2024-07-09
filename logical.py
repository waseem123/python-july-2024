#and operator
x = 100
y = 50
print((x>y) and (x>20))
print((x<y) and (x>20))
print((x>y) and (x<20))
print((x<y) and (x<20))
print("_____________________")

print((x>y) or (x>20))
print((x<y) or (x>20))
print((x>y) or (x<20))
print((x<y) or (x<20))
print("_____________________")

print(not(x>y))
print(not(x<y))

print(not(x<y) and not(x>20))
print(not(not(x<y) and not(x>20)))
print("_____________________")