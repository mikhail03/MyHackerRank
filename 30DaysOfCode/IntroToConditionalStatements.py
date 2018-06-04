"""
Completed By: Mikhail

Task 
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Complete the stub code provided in your editor to print whether or not  is weird.

Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.
"""

#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(raw_input())
    
    if N % 2 != 0:
        print "Weird"
    elif N % 2 == 0 and (N >= 2 and N <= 5):
        print "Not Weird"
    elif N % 2 == 0 and (N >= 6 and N <= 20):
        print "Weird"
    elif N % 2 == 0 and N > 20:
        print "Not Weird"


