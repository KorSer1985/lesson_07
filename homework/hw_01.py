# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для
# формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = list_of_lists

    # def __str__(self):
    #     string = ""
    #     for i in self.matrix:
    #         for el in i:
    #             string = f"{string}{el}\t"
    #         string = string[:] + "\n"
    #     return string

    def __str__(self):
        for i in self.matrix:
            for el in i:
                print(f"{el:5}", end="")
            print()
        return ''


    def __add__(self, other):
        for i in range(len(self.matrix)):
            for num in range(len(other.matrix[i])):
                self.matrix[i][num] = self.matrix[i][num] + other.matrix[i][num]
        return Matrix.__str__(self)


a = Matrix([[55, 17, 8], [8, 9, -34], [-16, 5, -22]])
m = Matrix([[55, -75, 6], [-47, -35, 4], [75, 3, 64]])
print(a.__add__(m))
