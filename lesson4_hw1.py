from sys import argv


def income(hours, rate, bonus):
    return hours * rate + bonus


h, r, b = map(float, argv[1:])

print(income(h, r, b))
