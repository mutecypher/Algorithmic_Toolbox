# python3
import random

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_fast(numbers):
    max_product = 0
    maxnumb = max(numbers)
    numbers.remove(max(numbers))
    sec_max = max(numbers)
    max_product = maxnumb * sec_max
    return  max_product


while True:
    n = random.randint(2, 1000)
    numbers = random.sample(range(2, 100000), n)
    ##print("the array is ", numbers,'\n')
    
    if max_pairwise_product(numbers) == max_pairwise_product_fast(numbers):
        print("OK",'\n')
    else:
        print("max_pairwise_product is ", max_pairwise_product, "and max_pairwise_product_fast", max_pairwise_product_fast)
        print('\n')
        break
    

