mylist = list((145,256,378,489,147,158,169))
print(mylist)
print(type(mylist))
print('___________________')

students = list()
for i in range(7):
    s = input("ENTER NAME OF STUDENT - ")
    students.insert(0,s)
print(students)