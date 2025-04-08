#example1
print("Hello")
print('Hello') #are the same thing

#example2
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"') #can use quotes inside a string, as long as they don't match the quotes surrounding the string

#example3
a = "Hello"
print(a) #assign string to a variable

#example4
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a) #are the same thing too

#example5
a = "Hello, World!"
print(a[1]) #Get the character at position 1 (remember that the first character has the position 0)

#example6
for x in "banana":
  print(x)
  
"""
prints:
b
a
n
a
n
a
"""

#example7
a = "Hello, World!"
print(len(a)) #gives the length of a string(including spaces)

#example8
txt = "The best things in life are free!"
print("free" in txt) #Check if "free" is present in the following text

#example9
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.") 

#example10
txt = "The best things in life are free!"
print("expensive" not in txt) #Check if "expensive" is NOT present in the following text

#example11
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#SLICING

#example12
b = "Hello, World!"
print(b[2:5]) #Get the characters from position 2 to position 5 (not included)-Output is "llo"

#example13
b = "Hello, World!"
print(b[:5]) #Get the characters from the start to position 5 (not included)

#example14
b = "Hello, World!"
print(b[2:]) #Get the characters from position 2, and all the way to the end

#example15
b = "Hello, World!"
print(b[-5:-2]) #Use negative indexes to start the slice from the end of the strin

"""
Get the characters:

From: "o" in "World!" (position -5)

To, but not included: "d" in "World!" (position -2)

prints:orl
"""
