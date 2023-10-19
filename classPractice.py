class Car:

    def __init__(self, brand, model, color):
        self.engine = None
        self.brand = brand
        self.model = model
        self.color = color

    def general_info(self, engine):
        self.engine = engine
        print(f"The {self.brand} {self.model} comes in a outstanding {self.color} and a powerful {self.engine} engine")


class ElectricCar(Car):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)
        self.engine = None

    def general_info(self, engine):
        self.engine = engine
        print(f"The {self.brand} {self.model} comes in {self.color} and {self.engine}")


porsche = Car('Porsche', '911', 'ruby red')
porsche.general_info('V8')

tesla = ElectricCar('Tesla', 'Model s', 'white')
tesla.general_info('No engine! it\'s electric')
