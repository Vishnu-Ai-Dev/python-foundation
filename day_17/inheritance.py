print("inheritance day 17 started")

#basic concept of inheritance  

'''class vehicle:
    def start(self):
        print("the vehicle is starting")

class car(vehicle):
    def drive(self):
        print("car is driving")

c=car()
c.start()
c.drive()'''

#another example for the inheritance class inheriting the the properties from the another class 

'''class fate:
    def holygrail(self):
        print("holy grail war is starting")

class servant(fate):
    def heros(self):
        print("gilgamesh is being summoned")

c=servant()
c.heros()
c.holygrail()'''


#creating a drone like inheritance code

class autonomous_robot:
    def __init__(self,designation):
        self.desgination=designation
        self.battery=100
    def boot_sequence(self):
        print(f"[{self.desgination}] system online battery is at {self.battery}%")

class surveillance_drone(autonomous_robot):
    def deploy_camera(self):
        print(f"[{self.desgination}] Aerial camera is successfully deployed current battery is at{self.battery-20}%")

class stealth_drone(surveillance_drone):
    def combat(self):
        print(f"mongrel detected! now tracking for better striking position remaining battery {self.battery-50}%")

king_of_heros=surveillance_drone("fuyuki")
king_of_heros=stealth_drone("fuyuki")

king_of_heros.deploy_camera()
king_of_heros.combat()

