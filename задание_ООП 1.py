class Transport:
    
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
class Bus(Transport):
    
    def __init__(self, name, max_speed, mileage, passengers):
        super().__init__(name, max_speed, mileage)
        self.passengers = passengers
        
    def __str__(self):
        return "Марка: "+self.name+" Макс. скорость: "+str(self.max_speed)+" Пробег: "+str(self.mileage)+" Вместимость: "+str(self.passengers)
        
 
 
bus=Bus("Renault Logan", 180, 12,10)
print(bus)