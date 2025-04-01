# 1. Naming Conventions

# Correct
class MyClass:
    def my_function(self):
        my_variable = 10

# Wrong
class my_class:
    def MyFunction(self):  
        MyVariable = 10  

# 2. Indentation

# Correct
if True:
    print("Hello")

# Wrong (uses tabs)
if True:
	print("Hello")  

# 3. Line Length

# Correct
def my_function():
    result = (10 + 20 + 30 + 40 + 50 +
              60 + 70)

# Wrong
def my_function():
    result = 10 + 20 + 30 + 40 + 50 + 60 + 70 + 80 + 90 + 100  

# 4. Spaces Around Operators

# Correct
a = b + c
d = (a + b) * c

# Wrong
a=b+c  
d = ( a+b )*c  
# 5. Blank Lines

# Correct

def first_function():
    pass


def second_function():
    pass

# Wrong
def first_function():
    pass
def second_function():  
    pass

# 6. Imports

# Correct
import os
import sys

# Wrong
import os, sys  

# 7. Docstrings & Comments

# Correct
def my_function():
    """This function does something."""
    pass

# Wrong
def my_function(): 
    pass

# 8. Avoid Unnecessary Whitespace

# Correct
x = 5
y = 10

# Wrong
x = 5   
y = 10   
