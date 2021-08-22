def user_data (name, last_name, phone, city, yob, email):
    print(name, last_name, yob, city, email, phone)


name = input("Введите имя: ")
phone = input("Введите телефон: ")
yob = input("Введите год рождения: ")
email = input("Введите email: ")
city = input("Введите город проживания: ")
last_name = input("Введите фамилию: ")

user_data(name = name, last_name = last_name, phone = phone, city = city, yob = yob, email = email)
