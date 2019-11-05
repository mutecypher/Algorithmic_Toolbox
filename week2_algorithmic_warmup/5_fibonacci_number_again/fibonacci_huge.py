# Uses python3
import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")
    
    
import numpy as np
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def calc_fib(n):
    if (n <= 1):
        return n
    fibs = [0] *( n + 1)
    list(enumerate(fibs))
    fibs[0] = 0
    fibs[1] = 1
    k = 2
    for k in range (2,n+1):
        fibs[k] = int(fibs[k-1]) + int(fibs[k-2])
    return fibs[k]



def mo_fib(n):
    numb = np.power((1+ np.sqrt(5))/2, n)/np.sqrt(5)
    return(int(np.floor(numb)))

porco_rosso = (mo_fib(n) - calc_fib(n))/calc_fib(n)

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(int(calc_fib(n)))
    print("the integer of the formula is", int(mo_fib(n)))
    print(calc_fib(n) % m)
    print("the difference is", porco_rosso)
