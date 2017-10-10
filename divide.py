# -*- coding: utf-8 -*-

dividend = int(input("Enter an integer dividend.\n"))
divisor = int(input("Enter an integer divisor.\n"))
quotient = dividend // divisor
remainder = dividend % divisor
print("%d is the quotient and %d is the remainder." % (quotient, remainder))

