"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
#example1
x = 5
print(type(x))

"""
x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType
"""

#NUMBERS

#example2
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#example3
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z)) #it all gives integer output

#example4
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z)) #Float can also be scientific numbers with an "e" to indicate the power of 10.

#example5
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z)) #Complex numbers are written with a "j" as the imaginary part

#example6 

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c)) #Convert from one type to another

#example7

import random

print(random.randrange(1, 10)) #Import the random module, and display a random number from 1 to 9:


#CASTING

#example1
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#example2
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#example3
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
