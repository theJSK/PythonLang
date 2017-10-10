# -*- coding: utf-8 -*-
"""

@author: Jung Soo
"""
firstInteger = int(input("Enter an integer.\n"))
secondInteger = int(input("Enter a second integer.\n"))
sum = 0
if secondInteger > 0:
    while secondInteger > 0:
        sum += firstInteger
        secondInteger -= 1
        continue
elif secondInteger < 0:
    while secondInteger < 0:
        sum -= firstInteger
        secondInteger += 1 
        continue
else: sum == 0
print(sum)
