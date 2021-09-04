a_mass_per_m = 25
thick = input('Please enter desired thickness of covering in cm: ')


class Road:
    def __init__(self, length, width):
        self._l = length
        self._w = width

    def tarmac(self):
        asphalt = (float(self._l) * float(self._w) * a_mass_per_m * float(thick)) / 1000
        return asphalt


r1 = Road(22000, 100)
print(r1.tarmac())
