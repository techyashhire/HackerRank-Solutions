#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def generate_string(s):
    n = len(s)
    pairs = 0
    st = list(s)
    
    for i in range(n - 1):
        if st[i] == st[i + 1]:
            st[i] = st[i + 1] = ''
            pairs += 1
    
    s = "".join([i for i in st if i != ''])
    
    return (pairs, s)
    

def superReducedString(s):
    pairs, result = generate_string(s)
    
    if pairs != 0:
        return superReducedString(result)
    
    return result if result else "Empty String"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
