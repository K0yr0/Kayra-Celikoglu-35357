animals = [
    {"name": "cat", "group": "mammal", "number_of_legs": 4, "skills": ["climbing", "jumping"]},
    {"name": "dog", "group": "mammal", "number_of_legs": 4, "skills": ["running", "swimming"]},
    {"name": "eagle", "group": "bird", "number_of_legs": 2, "skills": ["flying"]},
    {"name": "frog", "group": "amphibian", "number_of_legs": 4, "skills": ["jumping", "swimming"]},
    {"name": "snake", "group": "reptile", "number_of_legs": 0, "skills": ["slithering", "swimming"]},
    {"name": "shark", "group": "fish", "number_of_legs": 0, "skills": ["swimming"]},
    {"name": "butterfly", "group": "insect", "number_of_legs": 6, "skills": ["flying"]},
    {"name": "spider", "group": "arachnid", "number_of_legs": 8, "skills": ["climbing", "web spinning"]},
]

for animal in animals:
    skills_text = ", ".join(animal["skills"]) if animal["skills"] else "none"
    print(f"{animal['name'].title()} is a {animal['group']} with {animal['number_of_legs']} legs and can {skills_text}.")
