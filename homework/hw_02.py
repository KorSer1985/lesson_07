# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def costs(self):
        return f"Amount of fabric spent: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}"

    @abstractmethod
    def abstract(self):
        return "Abstract"


class Coat(Clothes):
    def costs(self):
        return f"To sew a coat, you need: {round(self.param / 6.5 + 0.5, 2)} cloth"

    def abstract(self):
        return "Abstract coat"


class Costume(Clothes):
    def costs(self):
        return f"To sew a suit, you need: {round(2 * self.param + 0.3, 2)} cloth"

    def abstract(self):
        pass


coat = Coat(255)
costume = Costume(78)
print(costume.costs())
print(coat.costs())
print(coat.abstract())
