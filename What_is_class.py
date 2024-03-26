"""Простеший класс и что внутри
   атрибут __dict__,__class__"""


class Simple: pass


if __name__ == '__main__':
    """Создание атрибутов класса виртуально без экз.класса"""
    Simple.name = 'Vika'
    Simple.age = 41
    print(Simple.name, Simple.age)
    """Создание экз.класса"""
    X = Simple()
    Y = Simple()

    print(X.name)  # Появляются атрибуты взятые из класса
    print(Y.name)  # Появляются атрибуты взятые из класса

    X.name = 'Илья'  # X Получает собственный атрибут

    print(X.name)
    print(Y.name)

    """Aтрибут __dict__"""
    print(list(Simple.__dict__.keys())) # ['__module__', '__dict__', '__weakref__', '__doc__', 'name', 'age']
    print(list(X.__dict__.keys())) # Х- Собственный атрибут name
    print(list(Y.__dict__.keys())) # Y- Отсутствуют атрибуты
    print(X.__dict__['name']) # Обращение к атрибуту через словарь
    print(X.__class__) # Показывает связь с классом

