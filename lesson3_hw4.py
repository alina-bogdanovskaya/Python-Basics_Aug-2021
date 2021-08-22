def my_func_negative_power_1(x, y):
    return x**y


def my_func_negative_power_2(x, y):
    return 1 / (x**abs(y))


def my_func_negative_power_3(x, y):
    a = abs(y)
    b = x
    while a > 1:
        b = b * x
        a -= 1
    return 1 / b


def my_func_negative_power_4(x, y):
    b = x
    for i in range(1, abs(y)):
        b = b * x
    return 1 / b


x = float(input("Please enter real positive number: "))
y = int(input("Please enter negative integer: "))

print(my_func_negative_power_1(x, y))
print(my_func_negative_power_2(x, y))
print(my_func_negative_power_3(x, y))
print(my_func_negative_power_4(x, y))
