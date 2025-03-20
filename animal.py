class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills
    def describe(self):
        return f"{self.name} is a {self.group} with {self.number_of_legs} legs and can do {', '.join(self.skills)}."

if __name__ == "__main__":
    cat = Animal("Cat", "Mammal", 4, ["Climbing", "Jumping"])
    eagle = Animal("Eagle", "Bird", 2, ["Flying"])
    print(cat.describe())
    print(eagle.describe())
