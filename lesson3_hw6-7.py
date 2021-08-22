def int_func_title1(string):
    changed_string = ''
    uppercase = True
    for elem in string:
        if elem == ' ':
            changed_string += elem
            uppercase = True
        elif uppercase == True:
            ascii_num = ord(elem) - 32
            elem = chr(ascii_num)
            changed_string += elem
            uppercase = False
        else:
            changed_string += elem
    return changed_string


def int_func_title2(string):
    string_to_change = string.split()
    index = 0
    for elem in string_to_change:
        ascii_num = ord(elem[0]) - 32
        changed_symbol = chr(ascii_num)
        string_to_change[index] = changed_symbol+elem[1:]
        index += 1
    changed_string = ' '.join(string_to_change)
    return changed_string


my_string = input('Please enter any word or sentence: ')

print(int_func_title1(my_string))
print(int_func_title2(my_string))
