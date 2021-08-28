from random import randint

init_list = [randint(1, 251) for i in range(23)]

print(init_list)

res_list = [n for count, n in enumerate(init_list) if n > init_list[count - 1] and count > 0]

print(res_list)
