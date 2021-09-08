from abc import ABC, abstractmethod


class Garment(ABC):

    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def mat_quant(self):
        pass


class Coat(Garment):
    def __init__(self, volume):
        self.V = volume

    @property
    def mat_quant(self):
        result = self.V/6.5 + 0.5
        return result


class Suit(Garment):
    def __init__(self, height):
        self.H = height

    @property
    def mat_quant(self):
        result = 2 * self.H + 0.3
        return result


coat1 = Coat(50)
print(f'Расход ткани на пальто размера {coat1.V} составит {coat1.mat_quant:.2f}')

suit1 = Suit(1.89)
print(f'Расход ткани на костюм на рост {suit1.H} составит {suit1.mat_quant:.2f}')

print(f'Суммарный расход ткани составит {coat1.mat_quant + suit1.mat_quant:.2f}')
