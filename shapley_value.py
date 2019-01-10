# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 10:51:51 2018

@author: romashov_vi
"""

from scipy.special import factorial

COALITIONS = (
    set(), {1}, {2}, {3}, {4},
    {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4},
    {1, 2, 3}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4}, {1, 2, 3, 4}
)

def v(S):
    if S == set():
        return 0
    elif S == {1}:
        return 3
    elif S == {2}:
        return 1
    elif S == {3}:
        return 2
    elif S == {4}:
        return 4
    elif S == {1, 2}:
        return 4
    elif S == {1, 3}:
        return 5
    elif S == {1, 4}:
        return 8
    elif S == {2, 3}:
        return 3
    elif S == {2, 4}:
        return 5
    elif S == {3, 4}:
        return 6
    elif S == {1, 2, 3}:
        return 7
    elif S == {1, 2, 4}:
        return 10
    elif S == {1, 3, 4}:
        return 11
    elif S == {2, 3, 4}:
        return 8
    elif S == {1, 2, 3, 4}:
        return 13
    return 0

def check_superadditivity():
    for S in COALITIONS:
        for T in COALITIONS:
            if not S & T and not v(S | T) >= v(S) + v(T):
                print('Not superadditive S: {0}, T: {1}'.format(
                S,
                T
            ))
        return False
    print('Superadditive')
    return True

def check_convexity():
    for S in COALITIONS:
        for T in COALITIONS:
            if not v(S | T) + v(S & T) >= v(S) + v(T):
                print('Not convex S: {0}, T: {1}'.format(
                S,
                T
            ))
            return False
        print('Convex')
        return True
    
def find_Shapley():
    X = []
    N = 4
    for i in range(1, 5):
        x_i = sum([factorial(len(S) - 1) * factorial(N - len(S)) * (v(S) - v(S - {i})) 
                    for S in COALITIONS if i in S]) / factorial(N)
            X.append(x_i)
        print('Shapley Value: ' + str(X))
            
    if sum(X) == v({1, 2, 3, 4}):
        print('Group rationalization condition is ok')
    else:
        print('Group rationalization condition is not ok')
    try:
        for i in range(1, 5):
            if not X[i - 1] >= v({i}):
                raise Exception('Dont')
        print('The condition of individual rationalization is ok')
    except Exception as e:
        if str(e) == 'Dont':
            print('The condition of individual rationalization is not ok')
                    
if __name__ == "__main__":
    check_superadditivity()
    check_convexity()
    find_Shapley()
