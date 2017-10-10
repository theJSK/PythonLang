# -*- coding: utf-8 -*-
"""

@author: Jung Soo
"""
int_list = []
i = 0

while i < 10:
    integer = int(input("Enter an integer."))
    int_list.append(integer)
    i += 1
int_list.reverse()
print(int_list)
