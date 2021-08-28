def fact(n):
    factor = 1
    for num in range(1, n + 1):
        factor *= num
        yield factor


n = int(input('Please enter any number: '))

for el in fact(n):
    print(el)
