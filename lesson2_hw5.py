num_list = [6, 5, 3, 2, 2]

while True:
    try:
        user_number = int(input('Please enter number: '))
        if user_number < 1:
            print('Not a positive integer')
        elif user_number <= num_list[-1]:
            num_list.append(user_number)
        else:
            for index, num in enumerate(num_list):
                if user_number > num:
                    num_list.insert(index, user_number)
                    break
        print(num_list)
    except ValueError:
        break
