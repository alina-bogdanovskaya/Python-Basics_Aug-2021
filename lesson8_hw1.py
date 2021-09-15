
class Date:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def list_str(cls, date: str):
        date_list = list(map(int, date.split('-')))
        return date_list

    @staticmethod
    def date_valid(my_date_list):
        di = {30: [4, 6, 9, 11], 31: [1, 3, 5, 7, 8, 10, 12], 28: [2]}
        s = 0
        day = my_date_list[0]
        month = my_date_list[1]
        year = my_date_list[2]
        if month not in range(1, 13):
            print("Invalid month")
            return False

        if day < 1:
            print("Invalid day")
            return False

        for key, value in di.items():
            if month in value:
                s = key
                break

        if month == 2:
            if year % 4 == 0 and year % 100 != 0:
                s = s + 1
            elif year % 100 == 0 and year % 400 == 0:
                s = s + 1

        if s == 0:
            print("Month not found")
            return False

        if day > s:
            print("Month contains less days")
            return False

        return True


date1 = Date("1-12-2021")

a = Date.list_str("1-12-2021")
b = Date.list_str("29-2-2021")
c = Date.list_str("29-2-1900")
d = Date.list_str("8-13-2000")

if Date.date_valid(a) is True:
    print(a)

if Date.date_valid(b) is True:
    print(b)

if Date.date_valid(c) is True:
    print(c)

if Date.date_valid(d) is True:
    print(d)
