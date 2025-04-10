#example1
print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False

#example2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") #Print a message based on whether the condition is True or False

#example3
print(bool("Hello"))
print(bool(15)) #Evaluate a string and a number

#example4
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#example5
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"]) #The following will return True

"""
NOTE:
Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
"""

#example6
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) #The following will return False

#example7
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj)) #returns False

#example8
def myFunction() :
  return True

print(myFunction()) 
 
