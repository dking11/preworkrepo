# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:24:45 2021

@author: canal
"""

#So far all the code we created only runs once, however code can be encapsulated in a
#function to be run multiple times, and to be run with placeholder inputs
#ex1 greeting
def greet(name):
    print("hello " + name)
#the indented code runs every-time we call the function into existence
greet('joe')# "hello joe"
greet('sam')# "hello sam"
#functions can and usually do return a value this is not going to print, but can be assigned
#to a variable and printed
def add(num1,num2):
    return num1+num2
add(1,2) #no output
num_sum = add(1,2)
print(num_sum) # OUTPUT: 3


#assignment 4

names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]

def longestword():
    count = 0
    for i in names_list:
        if len(i) > count:
            count = len(i)
            word = i
    return(word)

big_name = longestword()

