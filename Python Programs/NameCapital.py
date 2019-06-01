#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    l=list(s)
    string=""
    l[0]=l[0].upper()
    for i in range(0,len(l)):
        if l[i]==" ":
            l[i+1]=l[i+1].upper()
    for j in range(0,len(l)):
        string+=l[j]
    return string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
