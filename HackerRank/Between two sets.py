#!/bin/python3

import math
import os
import random
import re
import sys
from fractions import gcd

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def gcd(a,b):
    # Return greatest common divisor
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    # Return lowest common multiple
    return a * b / gcd(a, b)

def GCD(terms):
    # Return gcd of a list of numbers
    result = terms[0]
    for i in range(1, len(terms)):
        result = gcd(result, terms[i])
    return result

def LCM(terms):
    # Return lcm of a list of numbers
    result = 1
    for t in terms:
        result = lcm(result, t)
    return result

def getTotalX(a, b):
    lcm_value = LCM(a)
    gcd_value = GCD(b)
    counter = 0
    multiple_lcm = lcm_value
    while multiple_lcm <= gcd_value:
        if (gcd_value % multiple_lcm) == 0:
            counter += 1
        multiple_lcm += lcm_value
    return counter

n, m = [int(points) for points in input().strip().split(' ')]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = getTotalX(a, b)
print(total)
