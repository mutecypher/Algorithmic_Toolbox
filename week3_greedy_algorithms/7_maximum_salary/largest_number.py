#Uses python3

import sys

##def largest_number(a):
##    print(a)
##    a.sort(reverse = True)
##    b = [str(i) for i in a]
##    s = ''.join(map(str, b))
##    res = int(s)
##    return res


##input = sys.stdin.read()
##m = int(input())
##data = input.split()
##a = int(data[1:])
##print(largest_number(a))



##from itertools import permutations
##import pandas as pd
import numpy as np



def largest_number(numbers):
    numbers = list(map(str, numbers))
    n = len(numbers)
    twos = [2] * n
    frame = np.array(numbers)
    frame = frame.astype(int)
##    print(frame.ndim)
##    frame = np.append(frame, twos)
##    frame = frame.reshape(n,1)
    frame = np.vstack(frame)
    twoze = np.array(twos)
    twoze = np.vstack(twoze)
    plame = np.column_stack((frame, twoze, frame))
    for i in range(0,n):
        if plame[i,0] <  10:
            plame[i,1] = 1
            plame[i,2] = 111 * plame[i,0]
        elif plame[i,0] <  100:
            plame[i,1] = 3
            plame[i,2] = 10 * plame[i,0] + (np.floor(plame[i,0]/10))          
    ColIndex = 2
 ##   plame = np.sort(plame, axis = ColIndex)
    plame = plame[plame[:,ColIndex].argsort()][::-1]
    b = plame[:,0]
    s = ''.join(map(str, b))
    res = int(s)
##    print(plame[0,2])
    return res

##if __name__ == '__main__':
n = int(input())
input_numbers = input().split()
assert len(input_numbers) == n
print(largest_number(input_numbers))
 