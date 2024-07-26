mylist = ['John', 'Suraj', 'Mayur', 'Hasan', 'Sanjana', 'Roger', 'Alex', 'Sam', 'Bob']
print(mylist)
mylist[2] = 'Mayur Survase'
print(mylist)

index = int(input("ENTER INDEX - "))

if index<len(mylist):
    value = input("ENTER VALUE - ")
    mylist[index] = value
    print("LIST DATA CHANGED SUCCESSFULLY")
else:
    
    print("INVALID INDEX, NO CHANGE IN THE LIST")

print(mylist)