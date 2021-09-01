import json

comp_profit = {}
avg_profit = {}
dict_list = []

try:
    with open('companies.txt', 'r') as companies:
        sum_profit = 0
        num_lines = 0
        for line in companies:
            line = line.strip('\n')
            my_list = line.split()
            key = my_list[0]
            profit = int(my_list[2]) - int(my_list[3])
            if profit > 0:
                sum_profit += profit
                num_lines += 1
            comp_profit[key] = profit
            x = sum_profit / num_lines
            avg_profit['average profit'] = x
        dict_list.append(comp_profit)
        dict_list.append(avg_profit)
        print(dict_list)
except IOError as err:
    print(f'IOError: {err}')

with open('companies.json', 'w') as w_f:
    json.dump(dict_list, w_f)
