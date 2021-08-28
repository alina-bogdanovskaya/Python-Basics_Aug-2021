from random import randint


def list_unique_elem(list):
    freq_dict = {}

    for el in list:
        freq_dict[el] = freq_dict.get(el, 0) + 1

    for key, val in freq_dict.items():
        if val == 1:
            yield key


random_list = [randint(1, 20) for i in range(31)]
print(random_list)

unique_list = [k for k in list_unique_elem(random_list)]
print(unique_list)
