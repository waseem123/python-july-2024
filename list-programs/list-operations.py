mylist = ['Lion','Tiger','Leopard','Monkey','Lion','Bear','Wolf','Lion','Dog','Elephant','Fox']
print(mylist)
# to reverse the list use reverse() function
mylist.reverse()
print(mylist)

# sort() is used for sorting the elements of list in ascending or descending order
#to sort elements in descending order put reversed = true
mylist.sort(reverse=True)
print(mylist)

# sort() and reverse are permenant operations. they will change list items position permanantly

# index() function is used for identifying the index number of any element of the list. 
# it will give the index where the element has appeared for first time
print(mylist.index('Lion'))

# count() function is used for checking how many times the value is occuring in the list
print(mylist.count('Lion'))

# Repeats the occurance of the elements in the list for given muliple value
print(mylist*4)

l2 = ['cat','horse','donkey','rabbit']
print(l2)

# to append multiple elements in one list from another list use extend function
mylist.extend(l2)
print(mylist)
print(l2)

l1 = ['Zebra','Panda','Dolphin']
l3 = l1 + l2
print(l3)