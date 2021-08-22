def my_func_sum_max1(num1, num2, num3):
    num_list = [num1, num2, num3]
    return sum(num_list) - min(num_list)


def my_func_sum_max2(num1, num2, num3):
    min_val = min(num1, num2, num3)
    if num1 == min_val:
        my_sum = num2 + num3
    elif num2 == min_val:
        my_sum = num1 + num3
    else:
        my_sum = num1 + num2
    return my_sum


a = float(input("Введите значение: "))
b = float(input("Введите значение: "))
c = float(input("Введите значение: "))

print(my_func_sum_max1(a, b, c))
print(my_func_sum_max2(a, b, c))