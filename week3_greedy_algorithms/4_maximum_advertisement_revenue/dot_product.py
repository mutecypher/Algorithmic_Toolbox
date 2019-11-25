#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    ColIndex = 0
    a.sort()
##    print(a)
    b.sort()
##    print(b)
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


n = int(input())
prices = list(map(int, input().split()))
clicks = list(map(int, input().split()))
assert len(prices) == len(clicks) == n
print(max_dot_product(prices, clicks))
