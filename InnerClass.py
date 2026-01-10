class Car:
    def __init__(self, name):
        self.name = name;
    def show (self):
        print("Car name is", self.name)
    class Engine:
        def __init__(self, engine_name):
            self.engine_name = engine_name;
        def show(self):
            print("Engine name is", self.engine_name)

carObject = Car("Toyota")
carEngineObject = carObject.Engine("1.8")
carObject.show()
carEngineObject.show()  