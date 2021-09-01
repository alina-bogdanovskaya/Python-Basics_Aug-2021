try:
    with open('numbers_file.txt', 'w+') as num_file:
        x = '2 12 85 0 6'
        num_file.write(x)
        num_file.seek(0)
        num_list = num_file.read().split()
        num_sum = sum(map(int, num_list))
        print(num_sum)
except IOError as err:
    print(f'IOError: {err}')
