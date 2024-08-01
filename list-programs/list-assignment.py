mylist = ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
# for i in range(10):
#     mylist.append(input("Enter Value - "))
print(mylist)
print("________________")
for i in mylist:
    print(i)
print("________________")
for i in range(len(mylist)):
    print(f'{i}->{mylist[i]}')
    
print("________________")
for i in range(0,len(mylist),2):
    print(mylist[i])
    
print("________________")

print(mylist[5:10])
print(mylist[0:7:3])
mylist.pop()
print(mylist)
mylist.insert(4,35)
print(mylist)
print(mylist[-3:]
      )