# Uses python3
import numpy as np
def calc_fib(n):
    if (n <= 1):
        return n
    fibs = np.empty(n+1)
    fibs[0] = 0
    fibs[1] = 1
    k = 2
    for k in range (2,n+1):
        fibs[k] = int(fibs[k-2]) + int(fibs[k-1])
    return int(fibs[k])

n = int(input())
print(calc_fib(n))
