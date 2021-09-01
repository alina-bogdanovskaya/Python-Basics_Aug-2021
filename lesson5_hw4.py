num_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'}

try:
    with open('eng_numbers.txt', 'r', encoding='utf8') as num_eng:
        with open('rus_numbers.txt', 'w', encoding='utf8') as num_rus:
            for line in num_eng:
                list_line = line.split()
                a = list_line[0]
                b = num_dict.get(a)
                line_new = line.replace(a, b)
                num_rus.write(line_new)
except IOError as err:
    print(f'IOError: {err}')

with open('rus_numbers.txt', 'r', encoding='utf8') as num_rus:
    print(num_rus.read())
