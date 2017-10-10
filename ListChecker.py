# -*- coding: utf-8 -*-
"""
@author: Jung Soo
"""

int_list = []

i = 0
j = 0
inOrder = True
message = ""

while i < 10:
    integer = int(input("Enter an integer.\n"))
    int_list.append(integer)
    i += 1
"""print(int_list[j])"""

while j < 9:
    if (int_list[j] <= int_list[j + 1]):
        inOrder = True
        j += 1
        message = "Your list is in order."
    else: 
        inOrder = False
        message = "Your list is not in order."
        break
    
print(message)    
   
        