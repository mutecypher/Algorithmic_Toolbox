# python3


def max_pairwise_product_fast(numbers):
    max_product = 0
    maxnumb = max(numbers)
    numbers.remove(max(numbers))
    sec_max = max(numbers)
    max_product = maxnumb * sec_max
    return(max_product)

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))


