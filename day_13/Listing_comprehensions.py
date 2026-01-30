#listing normal method

'''numbers=[1,2,3,4,5]
squares=[]
for n in numbers:
    squares.append(n*n)
print(squares)'''

#creating a list of new value for each item in iterable

'''numbers=[1,2,3,4,5]
squares=[n*n for n in numbers]
print(squares)'''

#creating a list of new variables to show case the even numberss only by testing like adding the conditons

'''evens=[i for i in range(1,11) if i%2==0]
print(evens)'''

#one liner challange
#you run a shop you have a list a product of prices
#1.only keep the prices that are greater than 50
#2.Add 10% of tax to them

'''shop_price=[10,55,100,25,200,90]
shop_filter=[n*1.1 for n in shop_price if n>50]
print(shop_filter)'''

#Filtering a list which contain age greater than 18

age=[5,12,17,18,25,9,30]
filter_age=[n for n in age if n>=18]
print(filter_age)