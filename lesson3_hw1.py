def my_func_division(num, denom):
    try:
        result = num / denom
    except ZeroDivisionError:
        result = 'Cannot divide by zero'
    return result


num = float(input('Please enter numerator: '))
denom = float(input('Please enter denominator: '))

print(my_func_division(num, denom))
