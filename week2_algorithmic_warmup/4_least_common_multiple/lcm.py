# Uses python3
import sys

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


def lcm_naive(a, b):
    if a != 0 and b != 0:
        lcm = a * b / gcd_faster(a, b)
    else:
        lcm = 0
    return int(lcm)

##if __name__ == '__main__':
##    input = sys.stdin.read()
##    a, b = map(int, input.split())
##    print(lcm_naive(a, b))

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_naive(a, b))
