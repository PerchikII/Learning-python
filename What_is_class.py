"""Строковое представление: __rерr__ и __str__"""
class CS:
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return self.value + other

class Addrepr(CS):

    def __str__(self):
        return f'Объект класса {self.__class__.__name__}'

    def __repr__(self):
        return f'__repr__ {self.value}'


if __name__ == '__main__':
    F = Addrepr(4)
    print(F+5)
    print(F)
