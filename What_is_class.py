"""Второй пример"""


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



if __name__ == '__main__':
    X = First_class()
    Y = First_class()
    Z = Second_class()

    Z.set_data(1980)
    X.set_data("Илья")

    X.display()
    Z.display()
