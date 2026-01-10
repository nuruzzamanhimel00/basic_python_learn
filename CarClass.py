class Car:
    def __init__(self, name, age, year):
        self.name = name
        self.age = age
        self.year = year    
# carObject = Car("Toyota", 50, 2021)
# print(carObject.name)
# print(carObject.age)
# print(carObject.year)

class Toyota(Car):
    pass;

car = Toyota("Toyota", 50, 2021)
print(car.name)
print(car.age)
print(car.year) 