# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 10:51:51 2018

@author: romashov_vi
"""

import math
import bisect
import sys
from itertools import combinations

def main():
    characteristic_function = []
    shapley_values = []

    with open(sys.argv[1]) as gamefile:
        for line in gamefile:
            try:
                n = int(line[line.index('=') + 1:])
            except:
                print("Invalid file format")
                sys.exit(0)
            break
        for line in gamefile:
            characteristic_function = line.strip().split(",")
    tempList = list([i for i in range(n)])
    N = power(tempList)
    
    for i in range(n):
        shapley = 0
        for j in N:
            if i not in j:
                cmd = len(j)
                Ci = j[:]
                bisect.insort_left(Ci,i)
                l = N.index(j)
                k = N.index(Cui)
                temp = float(float(characteristic_function[k]) - float(characteristic_function[l])) *\
                           float(math.factorial(cmod) * math.factorial(n - cmod - 1)) / float(math.factorial(n))
                shapley += temp
        cmd = 0
        Ci = [i]
        k = N.index(Ci)
        temp = float(characteristic_function[k]) * float(math.factorial(cmd) * math.factorial(n - cmd - 1)) / float(math.factorial(n))
        shapley += temp
        shapley_values.append(shapley)
    print(shapley_values)
    
    if __name__ == '__main__':
    main()
    
def power(List):
    PS = [list(j) for i in range(len(List)) for j in combinations(List, i+1)]
    return PS
