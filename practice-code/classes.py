class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle=bodystyle
        
        
    def drive(self, speed):
        self.mode="driving"
        self.speed=speed
        
    def model(self, version):
        self.mode="Sports"
        self.version=version
                
class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels=4
        self.doors=4
        self.enginetype=enginetype
        
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed)
        
    def model(self, version):
        super().model(version)
        print("My Car has", self.doors, "wheels and version" ,self.version)
        
        
        
class Motorcycle(Vehicle):
    def __init__(self, enginetype, sidecar):
        super().__init__("Motorcycle")
        if(sidecar):
            self.wheels=3
        else:
            self.wheels=2
        self.doors=0
        self.enginetype =enginetype
        
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "Motorcycle at", self.speed)
        
    def model(self, version):
        super().model(version)
        print("my motorcycle has", self.wheels, "wheels and version", self.version)
        
        
car1=Car("gas")
car2=Car("electric")
mc1= Motorcycle("gas", False)


print(mc1.wheels)
print(car1.enginetype)
print(car2.doors)

car1.drive(30)
car2.drive(40)
mc1.drive(50)

car1.model("jaguar")
car2.model("hyundai")
mc1.model("Royal Enfield")