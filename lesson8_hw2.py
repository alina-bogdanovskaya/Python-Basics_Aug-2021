num = float(input("Please enter numerator: "))
denom = float(input("Please enter denominator: "))


class MyErr(Exception):
    def __init__(self, msg):
        self.msg = msg


try:
    if denom == 0:
        raise MyErr("Cannot divide by zero")
    print(num / denom)
except MyErr as err:
    print(err)
finally:
    print("Calculation complete")
