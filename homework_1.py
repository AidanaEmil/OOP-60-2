class Car:
  def __init__(self, brand, model, speed):
    self.brand=brand
    self.model=model
    self.speed=speed

  def description(self):
      return f"Машина: {self.brand} {self.model}, скорость: {self.speed} км/ч"

  def accelerate(self, increase):
     self.speed+=increase
     return f"Скорость увеличена до {self.speed} км/ч"

car1=Car("Toyota","Corolla",120)
car2=Car("BMW","X5",150)

print(car1.description())
print(car1.accelerate(20))

print(car2.description())
print(car2.accelerate(30))

