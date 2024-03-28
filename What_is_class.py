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
    def __init__(self, name, pay):
        Person.__init__(self, name, 'Менеджер', pay)

    def give_rise(self, percent, bonus=.10):
        return Person.give_rise(self, int(((self.pay / 100) * percent) + self.pay) * bonus)


class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def give_Raises(self, percent):
        for person in self.members:
            person.give_rise(percent)
    def showAll(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    ilya = Person('Абвгд Илья', 'Водитель', 2000)
    vika = Person('Аб_вгд Вика', 'Бухгалтер', 1500)
    ira = Manager('Абв_гд Ира', 300)

    devel = Department(ilya,vika)
    devel.give_Raises(100)
    devel.showAll()
    devel.addMember(ira)
    devel.showAll()
