# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 16:00:48 2021

@author: canal
"""


#Programming uses numbers, but thankfully you don't need to be a math genius to program. #Programming
#can be used to evaluate mathematical statements, you can also compare numbers to each-other #Ex1:
4+4
#Output: 8
#Ex2:
17<3
#OUTPUT: False
#We can also place a condition on the result of such a test:
#Ex2
example = 7
if example > 8:
    print("over")
else:
    print("under")
#OUTPUT: under
#You can do this to compare numbers to each-other
#Lastly we have lists and loops, a list is just a collection of strings, numbers, or other pieces of data
nums = [1,14,32,5,7]
#here we have a list of numbers we can write a for loop to list them out for us, note the indented
#command will run on all the numbers in the list num
for num in nums:
    print(num)
#Output:
#1
#14
#32
#5
#7
   
#assignment 2
    
overUlist = [1,45,32,21,5,17,43,93]   
for i in range(0,len(overUlist)):
    if overUlist[i] > 25:
        print("Over")
    elif overUlist[i] < 25:
        print("Under")