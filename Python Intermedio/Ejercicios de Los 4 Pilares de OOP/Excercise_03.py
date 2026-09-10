class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelarate(self, amount):
        if amount > 0:
            self.speed = self.speed + amount
            print(f'Acelero a {self.speed}')
        else:    
            print("Debe acelerar mayor a 0")

    
    def brake(self, amount):
        if self.speed - amount <= 0:
            print("Esta por debajo de la velocidad minima")
        else: 
            self.speed = self.speed - amount
            print(f'Desacelero a: {self.speed}')
        

class Electric:
    def __init__(self, battery_capacity, charge_level):
        self.battery_capacity = battery_capacity
        self.charge_level = charge_level

    def charge(self, amount):
        if self.charge_level + amount > self.battery_capacity:
            print("Ha sobre pasado el nivel maximo de carga")
        else:
            self.charge_level = self.charge_level + amount
            print(f'La bateria se cargo a: {self.charge_level}')
        
    def use_battery(self, amount):
        if self.charge_level - amount <= 0:
            print("Ha llegado al minimo de la bateria")
        else:
            self.charge_level = self.charge_level - amount
            print(f'El nivel de bateria bajo a: {self.charge_level}')
        

class ElectricCar(Vehicle, Electric):
    def __init__(self, brand, speed, battery_capacity, charge_level):
        Vehicle.__init__(self, brand, speed)
        Electric.__init__(self, battery_capacity, charge_level)

    def show_status(self):
        print(f"Marca del auto: {self.brand}")
        print(f"Velocidad actual: {self.speed}")
        print(f"Nivel de carga: {self.charge_level}")


car1 = ElectricCar("Tesla", 100, 200, 50)
car1.accelarate(50)
car1.brake(50)
car1.use_battery(15)
car1.charge(50)
car1.show_status()