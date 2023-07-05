# Working with Variables in Python to Manage Data
'''Concepts Practised
Printing to the Console in Python
String Manipulation and Code Intelligence
Debugging
The Python Input Function
Python Variables
Variable Naming'''


print("Welcome to the band name generator")

city = input("What city did you grow up in?\n")
pet = input("What is the name of your first pet?\n")
print("Your band name is " + city + " " + pet)
print("Your band name is", city, pet)

''' - - - - -- - - - - - - - - - - - - - - - - '''

name = "Sharad singh"
age = 23
add = "Mhow"
print(f'My name is {name} and I\'m {age} year\'s old. I live in {add}')
print('My name is {} and I\'m {} year\'s old. I live in {}'.format(name, age, add))
print('My name is {1} and I\'m {0} year\'s old. I live in {2}'.format(
    name, age, add))
# print("My name is " + name + " and i'm " + age + " year's old. I live in " + add) - this will error pf "TypeError: can only concatenate str (not "int") to str"
print("My name is " + name + " and i'm " +
      str(age) + " year's old. I live in " + add)


''' - - - - -- - - - - - - - - - - - - - - - - '''

name = input("What is your name\n").capitalize()
age = input("What is your age\n")
add = input("Where do you live\n").upper()
print("My name is " + name + " " + "I\'m" + " " + age +
      " " + "year's old." + " " + "I\'m from" + " " + add)
print("My name is " + name + " I\'m " + age +
      " year's old." + " I\'m from " + add)

''' - - - - -- - - - - - - - - - - - - - - - - '''

fname = input("Enter first name\n")
mname = input("Enetr middle name\n")
lname = input("Enter last name\n")

print(fname + " " + mname + " " + lname)
