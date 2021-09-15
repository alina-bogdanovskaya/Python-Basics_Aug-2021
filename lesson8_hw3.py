
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg


el = ''
dum_list = []

while True:
    el = input('Type something, to complete type "end" ')
    try:
        if el == "end":
            break
        try:
            el = float(el)
            dum_list.append(el)
        except ValueError:
            raise MyError("Only numbers will be added to the list")
    except MyError as err:
        print(err)

print(dum_list)
