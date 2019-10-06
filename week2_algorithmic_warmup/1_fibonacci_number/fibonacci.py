# Uses python3
import numpy as np
def calc_fib(n):
    if (n <= 1):
        return n
    fibs = np.empty(n)
    fibs[0] = 0
    fibs[1] = 1
    k = 2
    for k in range (2,n):
        fibs[k] = int(fibs[k - 1]) + int(fibs[k - 2])
        k = k + 1
    return int(sum(fibs))

n = int(input())
print(calc_fib(n))
