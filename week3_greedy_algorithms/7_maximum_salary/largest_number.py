#Uses python3

import sys

def largest_number(a):
    print(a)
    a.sort(reverse = True)
    b = [str(i) for i in a]
    s = ''.join(map(str, b))
    res = int(s)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

