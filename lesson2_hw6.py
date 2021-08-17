item_list = []
i = 0
item_key = 'наименование'
price_key = 'цена'
quant_key = 'количество'
unit_key = 'единицы'
item_dict = {}

while True:
    item = input('Введите наименование товара, чтобы закончить нажмите Enter: ')
    if item == '':
        break
    price = input('Введите цену товара: ')
    quant = input('Введите количество товара: ')
    unit = input('Введите единицы измерения товара: ')
    i += 1
    new_item = (i, {item_key: item, price_key: price, quant_key: quant, unit_key: unit})
    item_list.append(new_item)

print(item_list)

for tpl in item_list:
    for key in tpl[1].keys():
        value = tpl[1][key]
        value_list = item_dict.setdefault(key, [])
        if value not in value_list:
            value_list.append(value)

print(item_dict)
