# 5
# Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника. Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.
# 6
# Доработайте прошлую задачу. # Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

from sem10.task2 import Rectangle


class RectanglePro(Rectangle):
    """
    RectanglePro class doc
    """

    def __add__(self, other):
        """
        __add__ doc
        :param other:
        :return:
        """
        sum_of_perims = self.get_perim() + other.get_perim()
        a = self.a + other.a
        b = sum_of_perims / 2 - a
        return RectanglePro(a, b)

    def __sub__(self, other):
        """
        __sub__ doc
        :param other:
        :return:
        """
        if self.get_perim() < other.get_perim():
            self, other = other, self
        diff = self.get_perim() - other.get_perim()
        a = abs(self.a - other.a)
        b = diff / 2 - a
        return RectanglePro(a, b)

    def __eq__(self, other):
        """
        __eq__ doc
        :param other:
        :return:
        """
        return self.get_square() == other.get_square()

    def __gt__(self, other):
        """
        __gt__ doc
        :param other:
        :return:
        """
        return self.get_square() > other.get_square()

    def __le__(self, other):
        """
        __le__ doc
        :param other:
        :return:
        """
        return self.get_square() <= other.get_square()

    def __str__(self):
        return f'The RectanglePro. Side a: {self.a}. Side b: {self.b}'


if __name__ == '__main__':
    rect_1 = RectanglePro(2, 3)
    rect_2 = RectanglePro(5)
    print(rect_1.get_perim())
    print(rect_2.get_perim())
    rect_sum = rect_1 + rect_2
    rect_dif = rect_1 - rect_2
    print(rect_sum.get_perim())
    print(rect_sum.a, rect_sum.b)
    print(rect_dif.get_perim())
    print(rect_dif.a, rect_dif.b)
    print()
    print(rect_1.get_square())
    print(rect_2.get_square())
    print(rect_1 != rect_2)
    print(rect_1)
    print(help(RectanglePro))