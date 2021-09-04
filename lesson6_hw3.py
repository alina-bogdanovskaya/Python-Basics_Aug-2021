class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        total_income = sum(self._income.values())
        return total_income


p1 = Position("Peter", "Crowd", "Senior CRA", 30000, 3600)
print(p1.get_full_name())
print(p1.get_total_income())
print(p1.position + "\n")

p2 = Position("Mary", "Brown", "Clinical Lead", 50000, 25000)
print(p2.get_full_name())
print(p2.get_total_income())
print(p2.position + "\n")

p3 = Position("Catalina", "Amariei", "RM Portfolio Lead", 78000, 17300)
print(p3.get_full_name())
print(p3.get_total_income())
print(p3.position + "\n")
