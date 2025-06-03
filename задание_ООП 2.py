class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
    def seating_capacity(self, capacity):
        return f'Вместимость одного автобуса {self.name}  {capacity} пассажиров'
 
class Autobus(Transport):
    def __init__(self, name, max_speed, mileage, seating_capacity=50):
        super().__init__(name, max_speed, mileage)
 
    def seating_capacity(self, capacity=50):
        return f'Вместимость одного автобуса {self.name}: {capacity} пассажиров'
 
a = Autobus('Renault', 10, 10)
print(a.seating_capacity())