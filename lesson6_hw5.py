class Stationery:
    def __init__(self, title, color):
        self.title = title
        self.color = color

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки ручкой, цвет - {self.color}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки карандашом, цвет - {self.color}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки маркером, цвет - {self.color}")


red_pen = Pen("Stabilo", "красный")
red_pen.draw()

green_pencil = Pencil("Berlingo", "зеленый")
green_pencil.draw()

purple_handle = Handle("Copic", "лиловый")
purple_handle.draw()
