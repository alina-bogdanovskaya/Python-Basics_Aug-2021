
class ComplexNumber:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __add__(self, other):
        res_cn = ComplexNumber(self.real + other.real, self.img + other.img)
        return res_cn

    def __sub__(self, other):
        res_cn = ComplexNumber(self.real - other.real, self.img - other.img)
        return res_cn

    def __mul__(self, other):
        res_cn = ComplexNumber(self.real * other.real - self.img * other.img, self.img * other.real + self.real * other.img)
        return res_cn

    def __truediv__(self, other):
        res_cn = ComplexNumber((self.real * other.real - self.img * other.img) /
                               (other.real * other.real + other.img * other.img),
                               (self.img * other.real + self.real * other.img) /
                               (other.real * other.real + other.img * other.img))
        return res_cn

    def __str__(self):
        if self.img < 0:
            return f"{self.real} - {abs(self.img)}i"
        if self.real == 0:
            return f"{self.img}i"
        if self.img == 0:
            return f"{self.real}"
        return f"{self.real} + {self.img}i"


cn1 = ComplexNumber(2, 2)
cn2 = ComplexNumber(3, 3)
cn3 = ComplexNumber(2, -3)
cn4 = ComplexNumber(0, 2)
cn5 = ComplexNumber(5, 0)

print(cn1)
print(cn2)
print(cn3)
print(cn4)
print(cn5)
print(cn1 + cn2)
print(cn1 * cn2)
print(cn1 + cn3 + cn5)
print(cn1 * cn3)
print(cn4 * cn5 * cn2)
print(cn5 - cn3)
print(cn1 / cn2)
