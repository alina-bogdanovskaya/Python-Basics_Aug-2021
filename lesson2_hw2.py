el = ''
new_list = []

while True:
    el = input('Please enter list element, to complete press Enter: ')
    if el == '':
        break
    new_list.append(el)

print(new_list)

for index in range(0, len(new_list) -1, 2):
    new_list[index], new_list[index +1] = new_list[index +1], new_list[index]

print(new_list)