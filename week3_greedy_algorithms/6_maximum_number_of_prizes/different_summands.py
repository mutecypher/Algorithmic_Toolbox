# Uses python3
import sys
import numpy as np

def optimal_summands(n):
    start = np.sqrt(2*n)
    en = np.ceil(start)
    em = en.astype(int)
##    print('em is',em)
    grab = em*(em+1)/2
    grub = grab.astype(int)
##    print('grub is', grub)
    remove_em = grub - n
    remove_me = remove_em.astype(int)
    if remove_me == 0:
        summands = [i for i in range(1, int(em+1))]
##        print('lenght of summands is', len(summands))
    elif remove_me > em:
        summands = [i for i in range(1, int(em+1))]
        ek = em
        while remove_me  > ek:
            summands.pop(ek-1)
            remove_me = sum(summands) - n
            ek = ek - 1
        summands.pop(remove_me - 1)
    else:
        summands = [i for i in range(1, em+1)]
 ##       print(' index is', remove_me-1)
        summands.pop(remove_me - 1)
    return summands

##if __name__ == '__main__':
##    input = sys.stdin.read()
n = int(input())
summands = optimal_summands(n)
print(len(summands))
for x in summands:
    print(x, end=' ')
##print(sum(summands))
