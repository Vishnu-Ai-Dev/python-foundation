#using the build in libraris of python to test various kind of logic 

'''import math
print(math.sqrt(577)'''

'''import random
print(random.randint(1,10))'''

#Building a lottery system using the random library

import random

print("Welcome to grand carnival good luck with the lottery today")
try:
    enter_lottery=int(input("entery your three digit lottery:"))
except ValueError:
    print("invalid lottery please enter a valid one")
else:
    lucky_number=random.randint(100,699)
    print("today lucky number is:",lucky_number)

    if enter_lottery==lucky_number:
        print("yay you have won the lottery!")

    else:
        print("sorry this is not your lucky day try hard next time")