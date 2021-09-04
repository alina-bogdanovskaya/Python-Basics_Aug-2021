from time import sleep


class TrafficLight:
    __color = -1
    list_color = [{"color": "red", "time": 7}, {"color": "yellow", "time": 2}, {"color": "green", "time": 15}]

    def running(self):
        self.__color += 1
        if self.__color > 2:
            self.__color = 0
        state = self.list_color[self.__color]
        print(state["color"])
        sleep(state["time"])


crossroad_1 = TrafficLight()
for i in range(9):
    crossroad_1.running()
