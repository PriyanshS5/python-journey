name = input("Enter your name: ")
age = input("Enter your age: ")
#  Concatenate: to join two or more sequences—most commonly character strings—end-to-end to form a single longer sequence
age = int(age)    #can only concatenate str (not "int") to str thats why we converted str to int.
age = age+1

print(f" Hello {name}!")
print(f"You are {age} years old.")