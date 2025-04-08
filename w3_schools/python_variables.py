#example1
x = 5
y = "John"
print(x)
print(y)

#example2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x) #it will print x's last value that we assigned

#example3
x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

#example4
x = 5
y = "John"
print(type(x)) #it will give us which type is our variable
print(type(y))

#example5
x = "John"
print(x)
#double quotes are the same as single quotes:
x = 'John'
print(x)

#example6
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John" #all of these variable names are okay to use
#but these are not okay to use it will cause problems
2myvar = "John"
my-var = "John"
my var = "John"

#example7
myVariableName = "John" #camel case
MyVariableName = "John" #Pascal case
my_variable_name = "John" #snake caase

#example8
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z) #Note: Make sure the number of variables matches the number of values, or else you will get an error.

#example9
x = y = z = "Orange"

print(x)
print(y)
print(z) #it will all print same thing

#example10
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z) #it will print in order we wrote

#example11
x = "Python is awesome"
print(x) #it will give us= Python is awesome

x = "Python"
y = "is"
z = "awesome"
print(x, y, z) #it will also give us= Python is awesome

x = "Python "
y = "is "
z = "awesome"
print(x + y + z) #also the same result

#example 12
x = 5
y = 10
print(x + y) #it will do math

x = 5
y = "John"
print(x + y) #it is wrong because they are not the same type

#correct version
x = 5
y = "John"
print(x, y)

#example13
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc() #Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) #it will print= Python is fantastic Python is awesome

#example 14
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

