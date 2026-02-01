class car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        return 'Engine Started'  


my_car = car('toyota', 'blue') 
print(my_car.brand) 

print(my_car.start_engine())    
   