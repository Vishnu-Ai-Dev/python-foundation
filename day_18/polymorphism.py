print("day 18 polymorphism started")

#basic syntax polymorphism means the same name can behave differently depending upon the objects calling it 

'''class dog:
    def speak(self):
        print("bow")

class cat:
    def speak(self):
        print("meow")

animals=[dog(),cat()]
for a in animals:
    a.speak()'''

'''class bird:
    def sound(self):
        print("bird flies")

class aeroplane:
    def sound(self):
        print("aeroplane takes off")

sky=[bird(),aeroplane()]
for a in sky:
    a.sound()'''


class cnn:
    def train(self):
        print("[cnn] training vision matrix... identifying pixel patterns")

class rnn:
    def train(sself):
        print("[rnn] training sequential.. analyzing text flow")

class transformer:
    def train(self):
        print("[transformer]training attention mechanism.. processing full context<")

labmodels=[rnn(),cnn(),transformer()]
for ai_model in labmodels:
    ai_model.train()