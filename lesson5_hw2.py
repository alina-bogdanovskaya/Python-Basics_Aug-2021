try:
    with open('stuff.txt', 'r', encoding='utf8') as file:
        num_lines = 0
        num_words = 0
        for line in file:
            line = line.strip("\n")
            words = line.split()
            num_lines += 1
            print(f'words: {len(words)}')
        print("lines:", num_lines)
except IOError as err:
    print(f'IOError: {err}')
