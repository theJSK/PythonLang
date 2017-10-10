# -*- coding: utf-8 -*-
"""
@author: Jung Soo
"""
firstInteger = int(input("Enter an integer.\n"))
secondInteger = int(input("Enter a second integer.\n"))
operator = input("Enter an operator '+, -, *, /'.\n")
if (operator == '+'):
    answer = firstInteger + secondInteger;
    print("%d + %d = %d" % (firstInteger, secondInteger, answer))
elif (operator == '-'):
    answer = firstInteger - secondInteger;
    print("%d - %d = %d" % (firstInteger, secondInteger, answer))   
elif (operator == '*'):
    answer = firstInteger * secondInteger;     
    print("%d * %d = %d" % (firstInteger, secondInteger, answer)) 
elif (operator == '/'):   
    quotient = firstInteger // secondInteger
    remainder = firstInteger % secondInteger
    print("%d / %d = %d remainder %d" % (firstInteger, secondInteger, quotient, remainder))
else: print("Invalid operation.")