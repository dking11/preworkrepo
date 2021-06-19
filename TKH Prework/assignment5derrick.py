# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:32:27 2021

@author: canal
"""


#all strings and lists have individual characters and items respectfully represented by an index number
#this starts at 0, and can be accessed in bracket notation
thing = "car"
thing[0]#c
thing[2]#r
list = ["one",2,"3hree"]
list[2] # 3hree

#print both lists and then return the even one and print it again.

#assignment 5

names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
even = []
odd = []

def index():
    for i in names_list:
        if len(i)%2 == 0 :
            even.append(i)
        else:
            odd.append(i)
index()
print(odd)
print(even)
