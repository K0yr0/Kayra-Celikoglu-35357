my_age=19 #integer

coding_experience_year=4.5 #floating_point

name="Kayra" #strings

personal_data=[19,"Kayra",4.5] #lists

student = {
    "name": "Kayra",
    "age": 19,
    "grade": "5",
    "is_passed": True
}

print(student["name"]) 
print(student["grade"]) 

student["grade"] = "5"

student["course"] = "OOP"

for key, value in student.items():
    print(f"{key}: {value}") #dictionaries

my_tuples=(19,"Kayra",4.5) #tuples

name_surname=("Kayra","Celikoglu") #sets

is_raining = True  
has_umbrella = False  

if is_raining and not has_umbrella:  
    print("You will get wet!")  
else:  
    print("You are safe!")  #booleans
