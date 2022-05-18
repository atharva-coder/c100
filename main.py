class Car(object):
    
    def __init__(self,model,color,company,speed_limit,gear_type):
        self.color=color
        self.company=company
        self.model=model
        self.speed_limit=speed_limit
        self.gear_type=gear_type
    def start(self):
        self.speed_limit=100
        print("started")
    def acclerate(self):
        self.speed_limit+=20
        print("acclelrating")
    def changeGear(self):
        self.gear_type=3
        print("GearChanged")
        return 3
audi=Car("A6","red","audi",250,4)
print(audi.changeGear())        
           
