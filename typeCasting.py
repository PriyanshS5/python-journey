# Typecasting = The process of converting a value of one data type to another (String, integer, float, Boolean)
# Explicit vs Implicit

name = "bro"
age = 23
gpa = 3.2
student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(student))

#if the string is empty it is false means it will have 0 value in it so false.
# Bool gives false when the value is zero and if there is any other number present it will give true.

#Explicit 
#name  = int(name) #cant be done
# print(name)

age = float(age)
print(age)

gpa = int(gpa)
print(gpa)

name = bool(name)
print(name)

#Implicit Typecasting is  when the data type is converted automatically.

x = 2
y = 2.0

a = x + y

print(a)