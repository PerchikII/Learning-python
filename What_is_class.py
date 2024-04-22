"""Классы являются объектами:
    обобщенные фабрики объектов.
    Задачи ООП в Python решаются только с помощью объектов, полученных из классов."""


def factory(aClass, *pargs, **kargs):  # Кортеж или словарь с переменным
    return aClass(*pargs, **kargs)  # Вызывает aClass (или apply в Python 2.X)


class Spam:
    def doit(self, message):
        print(message)


class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job


if __name__ == '__main__':
    object1 = factory(Spam)  # Создать объект Spam
    object2 = factory(Person, 'Arthur', 'King')  # Создать объект Person
    objects = factory(Person, name=' Brian')

    object1.doit('Привет')
