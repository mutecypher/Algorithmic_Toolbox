# Uses python3
import sys
import numpy as np

def get_change(m):
    ## Get the number of 100's
    hundreds = float(np.floor(m/100))
##    print("after hundreds", m - 100*hundreds)
    ## get the number of 50'2
    fiftys = float(np.floor((m - int(100*hundreds))/50))
##    print("after fifties", m - (100*hundreds) - (50*fiftys))
    ## Get the number of 20's
    reduced_1 = m - (hundreds*100) - (50*fiftys)
    twenties = float(np.floor(reduced_1/20))
##    print("after 20's", reduced_1 - 20*twenties)
    ## Get the number of 10's
    tens = float(np.floor((reduced_1 - (20*twenties))/10))
##    print("after 10's", reduced_1 - (20*twenties) - (10*tens))
    ## Get the number of 5's
    reduced_2 = reduced_1 - (20*twenties) - (tens*10)
    fives = np.floor(reduced_2/5)
##   print("after 5's", reduced_2 - (5*fives))
    ##Get the number os 2's
    twos = np.floor((reduced_2 - (5*fives))/2)
    ## Get the number of 1's
##    print("after 2's", reduced_2 - (5*fives) - (2 * twos))
    ones = np.floor(reduced_2 - (5*fives) - (2*twos))
    ## Get the number of 50 cent
##   coins = 100*(reduced_2 - np.floor(reduced_2))
##    print("change", coins)
    if m <= 0:
        m = 0
    coins = m
    if m != 50:
        fif_coins = 0
    else:
        fif_coins = 0
##    print("after fifty cent pieces", coins - (50*fif_coins))
    ## Get the number of quarters
    if m != 25:
        quarters = 0
    else:
        quarters = 0
##    print("after quarters", (coins - (50*fif_coins) - (25*quarters)))
    
    ## get the number of dimes
    if m != 10:
        dimes = np.floor((coins - (50 * fif_coins) - (25 * quarters))/10)
    else:
        dimes = 0
    left = coins - (50 * fif_coins) - (25 * quarters) - (10*dimes)
    ## get the number of nickels
    if m != 5:
        nickels = np.floor(left/5)
    else:
        nickels = 0
    ## get the number of pennies
    pennies = np.rint(left - (5*nickels))
    changed = [ int(fif_coins), int(quarters), int(dimes), int(nickels)
    , int(pennies)]
    change = sum(changed)
    return change

m = float(input())
print(get_change(m))
