#magic method ..... start __somthing__

class bike:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    
    def __eq__(self, value):
        return self.name==value.name and self.color==value.color
    
    def __str__(self):
        return (f"Name + {self.name}, Color + {self.color}")
    
    def display(self):
        print(f"Name = {self.name}, Color = {self.color}")


bike1=bike("Yamaha","Blue")
bike2=bike("Yamaha","Blue")

print(bike1==bike2)#>,< aiso use korle uporer change kora lagbe
print(str(bike1))

