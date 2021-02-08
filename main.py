###### перегрузка операторов (магические методы) #######
"""
Мы хотим сравнивать две квартиры, но не просто по клочиству комнат, но по их качеству
(оценку качества задаете сами) с помощью переопредления сравнения
Пример сравнения по близости к школе и автобусу (и по площади).

"""
# class Flat:
#     __count_flat = 0
#     def __init__(self, rooms):
#         self._rooms = rooms
#         Flat.__count_flat += 1
#
#     def __len__(self):
#         return len(self._rooms)
#
#     def __add__(self, new_room):
#         #не возвращает новый объект, а изменяет первый
#         self._rooms.append(new_room)
#
#     def __str__(self):
#         return f'There are next rooms: {self._rooms}'
#
# first_flat = Flat(['kitchen', 'living room'])
# # print(first_flat)
# # print(len(first_flat))
# first_flat + 'bed room' #first_flat.add('bed room')
# print(first_flat)
#
# class District:
#     __count_districts = 0
#     def __init__(self, streets):
#         self._streets = streets
#         District.__count_districts+= 1
#
#     def __len__(self):
#         return len(self._streets)
#         # return 'Шел медведь по лесу, видит машина горит' не рабочая шалость
#         # return 42 рабочая шалость
#
#     def __del__(self):
#         print("I am deleted")
#     #
#     # def __delete__(self):
#     #     print("I am deleted ?")
#
#     def __add__(self, another_district):
#         #x = z + y где х - новый объект, z y - не изменились
#         District.__count_districts -= 1
#         new_dist = District(self._streets + another_district._streets)
#         # del another_district
#         # del self
#         return new_dist
#
#     def __str__(self):
#         return f'There are next streets: {self._streets}'
#
# Izmaylovo = District(['Izmaylovskaya', 'Leninskaya'])
# Zuzino = District(['Pervomayskaya', 'Nahimovskiy'])
#
# print(Izmaylovo)
# print(Zuzino)
#
# New_Vasuki = Izmaylovo + Zuzino
#
# print(len(New_Vasuki))
# print(New_Vasuki)
# print(Izmaylovo)
# print("Hi", Zuzino)

##### Интерфейс #######
from abc import ABC, abstractmethod

# class Docs_form(ABC):
#     @abstractmethod
#     def get_passport_data(self, passport):
#         pass
#
#     @abstractmethod
#     def get_credit_story(self):
#         pass
#
#     def print_hello(self):
#         print('Hello')
#
# class Visa_form(Docs_form):
#
#     def get_passport_data(self, passport):
#         pass
#
#     def get_credit_story(self):
#         pass
#
#     def print_hi(self):
#         return 'Hi'
#
# vasya_pupkin = Visa_form()
# print(vasya_pupkin.print_hi())
# vasya_pupkin.print_hello()

#Пример с прошлого занятия с обновленным кодом

# class Shape(ABC):
#     def __init__(self, color, param_1, param_2, rectangle_h = None):
#         print("I am new shape!")
#         self.color = color
#         self.param_1 = param_1
#         self.param_2 = param_2
#         self.rectangle_h = rectangle_h
#     @abstractmethod
#     def square(self):
#         return self.param_1 * self.param_2
#
# class Rectangle(Shape):
#     def square(self):
#         pass
#
# class Triangle(Shape):
#     """
#     s = 1/2*h*a
#     """
#     def square(self):
#         return 1/2 * self.param_1 * self.rectangle_h
#
# test_rectangle = Rectangle("white", 10, 20)
# print(test_rectangle.square())
#
# test_triangle = Triangle("orange", 30, 2, 7)
# print(test_triangle.square())

#### декоратор #####
# def beautiful_print(random_func):
#     def b_print():
#         print("* * * * * * * *")
#         random_func()
#         print("* * * * * * * *")
#     return b_print
#
# def print_hello():
#     print('Hello')
#
# x = beautiful_print(print_hello)
# x()
#


# @beautiful_print
# def print_hello_darling():
#     print('Hello, darling ')
#
# print_hello_darling()

###### декоратор @property ######

# class Mine:
#     def __init__(self):
#         self._x = 42
#
#
#     # способ взаимодействия с методом как с переменной
#     # формальный ввод защищенных переменных
#     #
#     @property
#     def x(self):
#         return self._x
#
#     @x.setter
#     def x(self, value):
#         self._x = value
#
#     @x.deleter
#     def x(self):
#         pass
#         # self._x = None
#
# test = Mine()
# print(test.x)
# a = test.x
# print(a)
# test.x = 6
# print(a)
# del test.x
# print(test.x)
#
# class TooManyGoods(ValueError):
#     def __init__(self, number, message):
#         result = number - 42
#         self.message = f'{message}. Please remove {result}'
#         super().__init__(self.message)
#
# class Box:
#     def __init__(self):
#         self.__weight = 0
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, new_weight):
#         if self.__weight + new_weight > 42:
#             raise TooManyGoods(self.__weight + new_weight, 'Too many goods')
#         # assert self.__weight + new_weight < 42  #хорошо для дебага по условию
#         self.__weight = self.__weight + new_weight
#
# b = Box()
# b.weight = 12
# print(b.weight)
# b.weight = 29
# print(b.weight)
# b.weight = 5
# print(b.weight)

###### Интерфейс итерации ######

# [1, 2, 3, 4]
class Iterator:
    def __init__(self, end = 0):
        #могжно вынеси в иттер, но фиксировать тогда end внутри кода
        self.i = 0
        self.all_files = []
        self.result = 0
        self.end = end

    def __next__(self):
        print("Hello, I am next")
        self.i += 1
        # current_data = pd.read_csv(self.all_files[i])
        self.result += 1
        if self.i <= self.end:
            return self.result
            # return current_data
        else:
            raise StopIteration

    def __iter__(self):
        print("Hello, I am iter")
        return self

itter_test = Iterator(5)
for el in itter_test:
    print(el)


