# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 16:28:38 2021

@author: canal
"""


#With your newfound skills we are going to add one new thing -- the len function.
#The len function will tell you the length of the string:
len("hello") #5
name = "joe"
len(name) # 3
#Create a script that loops through a list of names, comparing the length of each name to the
#length of all other names in the list finally printing out only the largest name
names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
#hint it should look something like this:
#longest_name = '' empty string as placeholder
#for name in names_list :

# if len(name)>longest_name:
# do something maybe reassign the longest name variable
# else:
# do another thing
#print longest_name
print(max(names_list, key = len))

#assignment 3

count = 0
for i in names_list:
    if len(i) > count:
        count = len(i)
        word = i
print(word)
