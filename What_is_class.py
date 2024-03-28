"""Добавление методов, реализующих поведение"""


class Person:
    """Персонаж может не иметь работы и соответственно зарплаты"""

    def __init__(self, name: str, job: str = None, pay: int = 0):  # Конструктор принимает три аргумента
        self.name = name
        self.job = job
        self.pay = pay

    def give_last_name(self):
        return self.name.split()[-1]

    def give_rise(self, percent):
        return int(((self.pay / 100)*percent) + self.pay)


    def __repr__(self):
        return f'Имя: {self.name.split()[-1]}\nДолжность: {self.job}\nЗП: {self.pay}'


ilya = Person('Илья', 'Bus', 2000)
vika = Person('Вика Алесина', 'Booh', 1500)
print(ilya.give_last_name(), ilya.give_rise(50))
print(vika.give_last_name(), vika.give_rise(20))
