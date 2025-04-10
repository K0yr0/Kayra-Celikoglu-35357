#MODIFY STRINGS

#example1
a = "Hello, World!"
print(a.upper()) #all uppercase

#example2
a = "Hello, World!"
print(a.lower()) #all lowercase

#example3
a = " Hello, World! "
print(a.strip()) #returns "Hello, World!" (Remove Whitespace)

#example4
a = "Hello, World!"
print(a.replace("H", "J")) #turns Hello to Jello

#example5
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


#STRING CONCANTENATION

#example6
a = "Hello"
b = "World"
c = a + b
print(c) #it will print HelloWorld without space

#example7
a = "Hello"
b = "World"
c = a + " " + b
print(c) #To add a space between them, add a " "

#STRING FORMAT

#example8
age = 36
txt = f"My name is John, I am {age}"
print(txt) #we can combine strings and numbers like this

#example9
price = 59
txt = f"The price is {price} dollars"
print(txt) #Add a placeholder for the price variable

#example10
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt) #The price is 59.00 dollars
