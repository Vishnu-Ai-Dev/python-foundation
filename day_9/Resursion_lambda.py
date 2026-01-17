'''print("day 9 recursion and lambda started")'''

#using recursion to do the factorial method 

'''def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))'''

#using recrusion to build the recursive fibonacci series

'''def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))'''

#using lambda for the one line logic and trying to use it as a pocket knife and use it as single line function tomake the codes cleaner
'''add_num=lambda n:n+n
print(add_num(4))'''

'''square_num=lambda n:n*n
print(square_num(5))'''

'''odd_even=lambda n: n %2==0
print(odd_even(10))
print(odd_even(17))'''

#creating a recursive sum using recursion 
def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
print(sum(6))

