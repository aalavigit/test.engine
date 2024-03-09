class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def display_info(self):
        return f"Engine Horsepower: {self.horsepower}hp"


class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    def display_info(self):
        return f"Car: {self.make} {self.model}\n{self.engine.display_info()}"


# Creating an Engine object
engine = Engine(200)

# Creating a Car object with the Engine component
car = Car("Toyota", "Camry", engine)

# Displaying information about the Car and its Engine
print(car.display_info())
