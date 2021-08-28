from itertools import count, cycle

for i in count(start = 3, step = -2):
    if i < -17:
        break
    print(i)

dum_list = 'London is the capital of Great Britain'.split(' ')
y = 1
for el in cycle(dum_list):
    if y > 13:
        break
    else:
        print(el)
    y += 1
