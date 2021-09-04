class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Car pulled away")

    def stop(self):
        print("Car stopped")

    def turn(self, direction):
        print(f"Car turned {direction}")

    def show_speed(self):
        print(f"Car speed is {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.is_police is False and self.speed > 60:
            print(f"Car speed is {self.speed}. Over speed limit")
        else:
            print(f"Car speed is {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Car speed is {self.speed}. Over speed limit")
        else:
            print(f"Car speed is {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


def car_info(my_car):
    if isinstance(my_car, PoliceCar) is True:
        print(f"This is a police {my_car.color} {my_car.name}")
    elif my_car.is_police is True:
        print(f"This is a civil {my_car.color} {my_car.name} used by police")
    else:
        print(f"This is a civil {my_car.color} {my_car.name}")


police1 = PoliceCar(90, "blue", "Lexus")
car_info(police1)
police1.go()
police1.show_speed()
print("")

work1 = WorkCar(55, "white", "SUV", False)
car_info(work1)
work1.turn("right")
work1.show_speed()
print("")

town1 = TownCar(55, "red", "VW", False)
car_info(town1)
town1.show_speed()
print("")

town2 = TownCar(75, "orange sunset", "Kia", False)
car_info(town2)
town2.show_speed()
print("")

town3 = TownCar(99, "silver", "Audi", True)
car_info(town3)
town3.show_speed()
print("")

sport1 = SportCar(120, "yellow", "Lamborghini", False)
car_info(sport1)
sport1.show_speed()
sport1.stop()
print("")
