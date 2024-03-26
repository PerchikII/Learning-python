"""Перегрузка, переопределение встроенных методов"""

class First_class(list):
    def __str__(self):
        return ' '.join(map(str,self))


if __name__ == '__main__':
    X = First_class([2,6,7,8])
    """Вывод встроенного класса изменился"""
    print(X)
