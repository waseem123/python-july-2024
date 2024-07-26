students = ['Suraj','Mayur','Hasan','Sanjana','Roger']
print(students)
print(len(students))
print(students[1])
print(students[3])

#using append() function
students.append("Alex")
students.append("Sam")
print(students)

# Using insert() function
students.insert(0,'John')
print(students)

students.insert(450,"Bob")
print(students)

value = input("ENTER YOUR NAME - ")
students.insert(3,value)
print(students)