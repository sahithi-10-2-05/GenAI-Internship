class Vehicle:
     def __init__(self,brand,model):
          self.brand=brand
          self.model=model

     def move(self):
        print("move")
   

class Car(Vehicle):
    def __init__(self,brand,model):
             self.brand=brand
             self.model=model
             self.fuel_type="Electric"
    def move(self):
             print("Car is driving on the road")

class Boat(Vehicle):
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        self.capacity=10
    def move(self):
        print(f"Boat is sailing with {self.capacity} passengers")

class Plane(Vehicle):
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        self.max_altitude=35000
    def move(self):
        print(f"Plane is flying at {self.max_altitude} feet")

class Drone(Vehicle):
    def __init__(self,brand,model):
             self.brand=brand
             self.model=model
             self.battery=15
    def move(self):
        if(self.battery>20):
            print("Drone is hovering")
        else:
            print("drone battery is low, cannot fly")

C1=Car("tesla","modelS")
B1=Boat("yamaha","waverider")
P1=Plane("Baeing","777")
D1=Drone("DJI","Min13")

print(C1.brand,C1.model,C1.fuel_type)
print(B1.brand,B1.model,B1.capacity)
print(P1.brand,P1.model,P1.max_altitude)
print(D1.brand,D1.model,D1.battery)

fleet=[C1,B1,P1,D1]
for v in fleet:
    v.move()

count=0
if("self.max_altitude>10000"):
     count+=1
if("self.capacity>0"):
     count+=1
if("self.battery>20"):
     count+=1
     print("active vehicles:",count)



     
     





         


