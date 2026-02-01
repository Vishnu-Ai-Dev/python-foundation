print("Day 14 revision started ")

#Dice roll simulator

'''Simport random
print("Dice roll simulater")
while True:
    dice=random.randint(1,6)
    print("rolling a dice:",dice)

    choice=input("do you want to roll more(yes/no):")
    if choice !="yes" :
        print("thanks for playing!")
    break'''

#Password generator

import random
alph="abcde"
password=""
for i in range(4):
    password+=random.choice(alph)
print(password)