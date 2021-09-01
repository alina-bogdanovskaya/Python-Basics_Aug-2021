try:
    with open('new_text_file.txt', 'w') as my_file:
        while True:
            content = input('Enter your data: ')
            if content == '':
                break
            else:
                my_file.write(content + '\n')
except IOError:
    print('Input output error')

with open('new_text_file.txt', 'r', encoding='utf8') as my_file:
    for line in my_file:
        print(line, end='')
