from re import sub

try:
    my_class_dict = {}
    with open('classes.txt', 'r') as classes:
        for line in classes:
            my_list = line.split()
            key = my_list[0]
            key = key[:-1]
            value_list = my_list[1:]
            hours = 0
            for i in value_list:
                if i != '-':
                    i = int(sub('\(.*?\)', '', i))
                    hours += i
            my_class_dict[key] = hours
except IOError as err:
    print(f'IOError: {err}')

print(my_class_dict)
