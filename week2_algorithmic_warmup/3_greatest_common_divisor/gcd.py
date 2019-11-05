# Uses python3
##import sys

##def gcd_naive(a, b):
##    current_gcd = 1
##    for d in range(2, min(a, b) + 1):
##        if a % d == 0 and b % d == 0:
##            if d > current_gcd:
##                current_gcd = d

def gcd_faster (a , b):
    remainder = 1
    while remainder != 0:
        if a >= b:
            big = a
            small = b
            remainder = big % small
            b = remainder
            a = small
        else:
            big = b
            small = a
            remainder = big % small
            a = remainder
            b = small
    return small

##if __name__ == "__main__":
##    input = sys.stdin.read()
##    a, b = map(int, input.split())
##    print(gcd_naive(a, b))

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(gcd_faster(a, b))
