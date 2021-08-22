res_sum = 0
stop = False

while stop != True:
    numbers = input('Please enter several numbers, press & to complete: ')
    if '&' in numbers:
        index = numbers.index('&')
        sum_list = sum(list(map(float, numbers[:index-1].split())))
        stop = True
    else:
        sum_list = sum(list(map(float, numbers.split())))
    res_sum += sum_list
    print(res_sum)
