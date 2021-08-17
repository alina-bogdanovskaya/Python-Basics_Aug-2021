my_str = input('Please enter few words: ')

for count, el in enumerate(my_str.split(), 1):
    if len(el) > 10:
        el = el[:10]
    print(f'#{count} {el}')
