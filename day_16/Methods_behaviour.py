#Creating simple classes using various real life example 

'''class student:
    def intro(self):
        print("hello my name is gojo")
s1=student()
s1.intro()'''

'''class car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def display(self):
        print("cars:",self.brand)
        print("speed:",self.speed)
s1=car("BMW","240kmph")
s1.display()'''


'''class laptop:
    def __init__(self,brand,RAM,price):
        self.brand=brand
        self.RAM=RAM
        self.price=price
    def display(self):
        print("Laptop:",self.brand)
        print("RAM:",self.RAM)
        print("Price is:",self.price)
s1=laptop("ASUS","16GB",75000)
s1.display()'''


#adding the line of math using the class concepts

class sorceror:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
    def fight(self,enemy,attack):
        if attack=="dismantle":
            enemy.hp=enemy.hp-20
        elif attack=="Fuga":
            enemy.hp=enemy.hp-50
        else:
            enemy.hp=enemy.hp
        print(f"{self.name} used {attack} on {enemy.name}")
        print(f"{enemy.hp} has been reduced due to the attack")
gojo=sorceror("gojo",1000)
sukuna=sorceror("sukuna",1000)
sukuna.fight(gojo,"dismantle")


class phone:
    def __init__(self,brand,battery):
        self.brand=brand
        self.battery=battery
    def display(self):
        print("The cellphone is:",self.brand)
        print("The battery is:",self.battery)
    def play_game(self,battery):
        if self.battery>=30:
            self.battery=self.battery-30
        print(f"playing genshin impact the battery is now {self.battery}")

        else
        print("low battery please charge the phone")
c1=phone("ASUS",100)
c1.display()
c1.playgame()