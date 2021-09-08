class Cell:
    def __init__(self, cellula: int):
        self.cel = cellula

    def __add__(self, other):
        res_cell = Cell(self.cel + other.cel)
        return res_cell

    def __sub__(self, other):
        if self.cel - other.cel < 0:
            raise Exception("Unable to calculate")
        res_cell = Cell(self.cel - other.cel)
        return res_cell

    def __mul__(self, other):
        res_cell = Cell(self.cel * other.cel)
        return res_cell

    def __truediv__(self, other):
        res_cell = Cell(round(self.cel / other.cel))
        return res_cell

    def __floordiv__(self, other):
        res_cell = Cell(self.cel // other.cel)
        return res_cell

    def __str__(self):
        return str(self.cel)

    def make_order(self, cel_per_line):
        num_ful_lines = self.cel // cel_per_line
        num_last_line = self.cel % cel_per_line
        line = ('*' * cel_per_line + '\n') * num_ful_lines + '*' * num_last_line
        if num_last_line != 0:
            line = line + '\n'
        return line


cell1 = Cell(13)
cell2 = Cell(4)
cell3 = Cell(7)

print(cell1 + cell2)

try:
    print(cell1 - cell2)
except Exception as err:
    print(f'Exception: {err}')

try:
    print(cell2 - cell3)
except Exception as err:
    print(f'Exception: {err}')

print(cell2 * cell3)

print(cell2 / cell1)

print(cell3 // cell2)

print(cell2 // cell1)

print(cell1.make_order(4))

print(cell2.make_order(2))

print(cell3.make_order(3))
