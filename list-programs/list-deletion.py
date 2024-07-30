mylist = ['Sanjana','Suraj','Hasan','Mayur','Nikhil','Waseem','Alex','Peter','John','Leo']
print(mylist)

#deleting last value from the list use pop()
mylist.pop()
print(mylist)
# delete value from any index use pop(index); 
# index should be in the range of list size
mylist.pop(3)
print(mylist)

# delete the value directly from list using remove(); 
# Value has to be present in the list for deletion
mylist.remove('Sanjana')
print(mylist)

del mylist[2]
print(mylist)

#Empty the list using clear()
mylist.clear()
print(mylist)

del mylist
print(mylist)
