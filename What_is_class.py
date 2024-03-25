class C1:
    """Суперкласс"""
    x = 5
    y = 10


class C2:
    """Суперкласс"""
    x = 1
    w = 2

    def __repr__(self):
        """Перегрузка метода"""
        return f'Объект класса {__class__.__name__}'


class C(C1, C2):
    """Подкласс"""
    a = 11
    y = 12

    def __init__(self, name: str):
        """Инициализация атрибутов класса"""
        self.name = name

    def __str__(self):
        """Перегрузка метода"""
        return f'Объект класса {__class__.__name__}'


E = C("Илья")  # Экз.класса
print(E.name)  # Обращение к атрибуту
E1 = C1()  # Экз.класса
E2 = C2()  # Экз.класса

print(E)
print(E1)
print(E2)
