#1-print your name on the screen
print("My name is Kayra")

#2-create 3 different type of variable(str,int...)
name = "Kayra"   # string
age = 19         # integer
height = 1.70     # float

#3-Display the type of the variable you created
print(type(name))
print(type(age))
print(type(height))

#4-Use if to check if a number is equal to 10. If yes, print "Ten"
number = 10
if number == 10:
    print("Ten")

#5-Create a list called fruits with any 3 fruit names. Then print the second fruit
fruits = ["apple", "banana", "cherry"]
print(fruits[1])  # Second fruit (index 1)

#6-Use an if statement to check if a variable x is equal to 100. If it is, print "Yes", otherwise print "No"
x = 100
if x == 100:
    print("Yes")
else:
    print("No")

#7-Make a dictionary called student with keys: "name", "age", and "grade". Assign values and print the age
student = {
    "name": "Sarah",
    "age": 18,
    "grade": "B"
}
print(student["age"])


#8-Add a new item "grape" to the fruits list from question 5 and print the updated list
fruits.append("grape")
print(fruits)


#9-Update the "grade" in the student dictionary to "A+" and print the full dictionary
student["grade"] = "A+"
print(student)

#10-Create a class Person with an attribute name. Add a method greet() that prints "Hello, " + name. Create an object and call greet()

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name)

person1 = Person("Kayra")
person1.greet()
