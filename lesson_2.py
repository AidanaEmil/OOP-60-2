class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    def drive(self, location):
        print(f'Car {self.model} is driving at {location}')
    def test(self):
        self.drive("Karakol")
class Bus(Car):
    pass