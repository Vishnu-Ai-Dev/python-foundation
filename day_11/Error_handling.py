print("day 11 Error handling starts")

#using the try and except trying to find the what happens when one conditions failed 

'''try:
    age=int(input("Enter your age:"))
    print("your next year age:",age+1)
except:
    print("you have entered a wrong input")'''

#using the try and except statement with the specifications 

'''try:
    x=int(input("Enter a number to divide the number ten:"))
    print("the value is: ",10/x)
except ValueError:
    print("you have entered a wrong value please enter a valid one!")
except ZeroDivisionError:
    print("please do not enter the number zero please enter a another one")'''

#using the try statement building the safe age input system

'''try:
    age=int(input("Enter your age:"))
    print("you are eligible for the website! redirecting into the homepage")
except ValueError:
    print("you have entered a wrong age please try with a valid one")'''

#Building a safe ATM MACHINE using the try and except statement and using the if block statements for enforcing the rules of the atm

print("        WELCOME TO XYZ BANK      ")

print("  Please enter your valid amount     ")
try:
    y=10000
    enter_amount=int(input("Enter your withdrawl amount:"))
    x=y-enter_amount
except ValueError:
    print("you have entered the wrong amount please enter a valid one")
else:
    if y>enter_amount:
        print("your amount is being transacted please wait")
    elif enter_amount>y:
        print("Insufficient balance")