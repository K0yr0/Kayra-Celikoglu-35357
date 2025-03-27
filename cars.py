class Engine:
    def __init__(self, horsepower, type):
        self.horsepower = horsepower
        self.type = type

    def get_info(self):
        return f"{self.horsepower} HP {self.type} Engine"


class Car:
    def __init__(self, brand, model, year, car_type, color, engine):
        self.brand = brand
        self.model = model
        self.year = year
        self.type = car_type
        self.color = color
        self.engine = engine

    def get_info(self):
        return f"{self.year} {self.brand} {self.model} ({self.type}) - {self.color}, {self.engine.get_info()}"


engine1 = Engine(450, "Petrol")
engine2 = Engine(670, "Hybrid")
engine3 = Engine(760, "Electric")

car1 = Car("Porsche", "911", 2023, "Coupe", "Silver", engine1)
car2 = Car("Ferrari", "488", 2021, "Sports", "Red", engine2)
car3 = Car("Ford", "Mustang", 2022, "Coupe", "Blue", engine3)

print(car1.get_info())
print(car2.get_info())
print(car3.get_info())
