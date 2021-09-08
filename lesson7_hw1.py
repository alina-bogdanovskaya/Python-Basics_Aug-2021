
class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        string = ""
        for i in self.matrix:
            for j in i:
                string = string + " " + str(j)
            string = string + "\n"
        return string

    def __add__(self, other):
        result_matrix = []
        for i in range(len(self.matrix)):
            result_matrix.append([])
            for j in range(len(self.matrix[0])):
                result_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(result_matrix)


m1 = Matrix([[1, 2, 3, 4], [4, 3, 2, 1], [2, 4, 5, 7]])
print(m1)

m2 = Matrix([[3, 6, 9, 11], [1, 8, 5, 2], [0, 3, 1, 4]])
print(m2)

m3 = Matrix([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]])
print(m3)

print(m1 + m2 + m3)
