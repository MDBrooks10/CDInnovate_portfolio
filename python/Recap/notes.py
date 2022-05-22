import random

##############
# Data types #
##############

# # print is how we display information in the terminal
# print("this is my current file")

# # strings are for representing characters
# print("Hello my name is klong")
# print("1234")

# #This is an interger - a whole number
# print(1234)

# #this is a floating point - anything with a decimal
# print(1234.5)

# #booleans - True and False
# print(True)
# print(False)

# #none - a blank, or null type
# print(None)


###########
# Methods #
###########

#We can use methods to manipulate data within variables

# #Len tells us how many characters are in the string
# print(len("hello"))

# #index position - starts count at 0
# print("hello"[1])

# # .notation is a way of accessing methods
# print("hello".upper())


#############
# Libraries #
#############

#Libraries give us access to more methods

# print(random.random())
# print(random.uniform(1,10))
# print(random.randint(1,10))
# print(random.randint(1,5))

# import random
# from random import random,randint,uniform

# print(uniform(1,10))


#############
# Variables #
#############

#Variables are like boxes that store information or data
#snake_case should be used to name variables with more than one word

# my_name = "Klong"
# my_age = 30

# print(my_name)

# print("Hello my name is",my_name)
# print("Hello my name is " + my_name)
# print("Hello my name is {}".format(my_name))
# print("Hello my name is {} and I am {} years old.".format(my_name,my_age))
# print(f"Hello my name is {my_name} and I am {my_age} years old.")


#############
# Operators #
#############

# print(1+2)
# print(2-1)
# print(2*3)
# print(3**3)
# print(15/3)
# print(15%3)

# balance = 100
# amount = 50

# print(balance-amount)
# balance = balance - amount
# balance -= amount
# print(balance)

# char_name = input("What is your name? > ")

# print(f"Welcome, {char_name}")

# music = "classical"

# if music == "classical":
#     print("Oh no it's classical!")
# elif music == "pop":
#     print("Turn it up")
# else:
#     print("Yay")

# print(10%2==0)

# num1=100
# num2=100

# if num1 > num2:
#     print("1 is bigger")
# elif num1 < num2:
#     print("2 is bigger")
# else:
#     print("1 and 2 are the same")

# num = 22

# if num%7==0 and num%3==0:
#     print("fizzbuzz")
# elif num%3==0:
#     print("fizz")
# elif num%7==0:
#     print("buzz")
# else:
#     print(num)

# place = "MCR"
# weather = "Sunny"

# if place == "MCR" and weather == "Sunny":
#     print("Check again")
# elif place == "MCR" and weather == "Rain":
#     print ("Obvs")
# else:
#     print ("Wait it isn't raining?")


# day = "Monday"
# bank_holiday = True

# if day == "Saturday" or day == "Sunday" or bank_holiday==True:
#     print("Yay it's a day off")
# else:
#     print("Time to go work")


#############
# Functions #
#############

# Functions typically take data, do something with it and return an output

# def light_switch():
#     print ("Who turned out the lights?")

# light_switch()

# def cash_withdrawal (amount, accnum):
#     print (f"Withdrawing £{amount} from account #{accnum}")

# cash_withdrawal(300, 5049856)
# cash_withdrawal(500, 45093485)
# cash_withdrawal(20, 3243455)

# def add_up(num1,num2):
#     return num1+num2

# print(add_up(5,2))


#########
# Lists #
#########

# coffee_order = [
#     "Alex - Cortado",
#     "Ben - Latte",
#     "Charlie - Whatever"
# ]

# print (coffee_order)

# fav_films = [
#     "Jurrasic Park",
#     "Shawshank Redemption",
#     "12 Angry Men"
# ]

# print(fav_films)

# fav_films[2] = "Spiderman"

# print(fav_films)

# fav_films.append("Godzilla")

# print(fav_films)

# fav_films.pop(2)

# print(fav_films)


# fav_drinks = ["coke", "fanta", "tonic", "coffee"]

# # for i in fav_drinks:
# #     print ("Nice")

# # for i in range(10):
# #     print(i)

# for i in range (2,12,2):
#     print(i)

# num=0

# while num < 10:
#     num += 1
#     print(num)