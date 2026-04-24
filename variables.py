# Variable : A container for a value (String, integer, float, boolean )
#            A  variable behaves as it was the value it contains

#Strings
first_name = "Priyansh"
fav_food = "Burger"
email = "priyansh.singh211@gmail.com"

print("Hello")
print(f"hello {first_name}") #it is called f-string (formatted String literals).
print(f"I like {fav_food}")  #it comes with f and curly braces to implement. 
print(f"My email is {email}") # call the variable and it will dispaly the stored value (literal).

#Integers
age = 22
quantity = 12
num_of_students = 30

print(f"I am {age} years old.")
print(f"I have to buy {quantity} Bananas.")
print(f"Your class has {num_of_students} students.")

#Float
germs = 99.99
gpa = 3.2
distance = 10

print(f"Lifbuoy soap kills {germs}% of germs.")
print(f"I have an aggregate of {gpa}.")
print(f"I cycled {distance} Kms.")

#Boolean
is_student = True
for_sale = False
is_online = True

if is_student:
    print("I am a student.")
else:
    print("I am not a student.")

if for_sale:
    print("I will go shopping.")
else:
    print("I will not be going to shopping.")    

if is_online:
    print("I will text her.")
else:
    print("I will not text her.")    
        