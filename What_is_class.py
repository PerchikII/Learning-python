"""Третий пример"""


class First_class:
    def set_data(self, value):
        self.data = value

    def display(self):
        print(f"Старый вывод {__class__.__name__}:{self.data}")


class Second_class(First_class):
    """Пример переопределение метода"""

    def display(self):
        """Переопределение метода"""
        print(f"Новый вывод {__class__.__name__}:{self.data}")


class Third_class(Second_class):
    def __init__(self, val):
        self.data = val

    def __add__(self, other):
        """выражение + в коде автоматом запускает метод __add__"""
        return Third_class(self.data + other) # Возвращает новый объект класса и запускает __init__

    def __str__(self):
        return f'{__class__.__name__}: {self.data}'

    def mul(self, other):
        """Изменяет значение атрибута"""
        self.data *= other


if __name__ == '__main__':
    X = Third_class('345')
    X.display()
    print(X)
    B = X + 'abc' # '+' автоматом запускает метод __add__
    B.display()
    print(B)
    X.mul(7)
    print(X)



