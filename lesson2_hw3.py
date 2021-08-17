#1
season_list = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer',
               'summer', 'summer', 'fall', 'fall', 'fall', 'winter']
month_list = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

month = int(input('Please enter month number: '))

if 0 < month <= 12:
    print(f'Your month is {month_list[month - 1]}, it is {season_list[month - 1]}')
else:
    print('Incorrect value')

#2
season_dict = {'winter': (1, 2, 12), 'spring': (3, 4, 5), 'summer': (6, 7, 8), 'fall': (9, 10, 11)}
month_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
              7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}

month = int(input('Please enter month number: '))
result = False

for key, value in season_dict.items():
    if month in value:
        result = True
        break

if result == True:
    print(f'Your month is {month_dict.get(month)}, it is {key}')
else:
    print('Incorrect value')