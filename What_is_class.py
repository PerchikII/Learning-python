"""Настройка поведения за счет
создания подклассов"""


class Person:
    """Персонаж может не иметь работы и соответственно зарплаты"""

    def __init__(self, name: str, job: str = None, pay: int = 0):  # Конструктор принимает три аргумента
        self.name = name
        self.job = job
        self.pay = pay

    def give_last_name(self):
        return self.name.split()[-1]

    def give_rise(self, percent):
        self.pay = int(((self.pay / 100) * percent) + self.pay)

    def __repr__(self):
        return f'Имя: {self.name.split()[-1]}\nДолжность: {self.job}\nЗП: {self.pay}'


class Manager(Person):
    def give_rise(self, percent,bonus=.10):
        return Person.give_rise(self,int(((self.pay / 100) * percent) + self.pay)*bonus)


if __name__ == '__main__':
    ilya = Person('Абвгд Илья', 'Bus', 2000)
    vika = Person('Аб_вгд Вика', 'Booh', 1500)
    ira = Manager('Абв_гд Ира', 'садик',200)
    # print(ilya.give_last_name(), ilya.give_rise(50))
    # print(vika.give_last_name(), vika.give_rise(20))
    # print(ira.give_last_name(), ira.give_rise(10))

    for obj in (ilya,vika,ira):
        obj.give_rise(25)
        print(obj)

