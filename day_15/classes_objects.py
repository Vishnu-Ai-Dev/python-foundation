'''print("day 15 oops started")'''

#Creating the firs student class

'''class Student:
    def __init__(self, name,age):
        self.name= name
        self.age= age

    def introduction(self):
        print("My name is:",self.name)
        print("My age is:",self.age)
s1=Student("Vishnu",18)
s1.introduction()'''

#creating sorceror class

'''class sorceror:
    def __init__( self, name,grade):
        self.name=name
        self.grade=grade
    def profile(self):
        print("my name is:", self.name)
        print("I am a :", self.grade)
s1=sorceror("gojo","special grade sorceror")
s2=sorceror("yuji","special grade sorceror")
s2.profile()'''

#creating a bank class 

'''class Bank_Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def customer_info(self):
        print("your name is:",self.name)
        print("you balance is:",self.balance)

c1=Bank_Account("Gilgamesh",5000000000000)
c2=Bank_Account("Shirou",600000)
c1.customer_info()'''


# deploying my own mini ai bot using classes

class Ai_Model:
    def __init__(self,name,personality):
        self.name=name
        self.personality=personality
    def speak(self):
        if self.personality=="friendly":
            print(f"oh hello there {self.name}, how can i help you today")
        elif self.personality=="rude":
            print(f"i dont like speaking with random mongrel {self.name} don'bother with me")
        else:
            print(f"{self.name} made a request currently in progress")
bot1=Ai_Model("Gemini","friendly")
bot2=Ai_Model("Gilgamesh","rude")
bot1.speak()
bot2.speak()