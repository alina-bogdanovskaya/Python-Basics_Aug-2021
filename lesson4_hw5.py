from functools import reduce


def product(factor1, factor2):
    return factor1 * factor2


init_list = [i for i in range(100, 1001) if i % 2 == 0]

print(init_list)
print(reduce(product, init_list))
