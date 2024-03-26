"""Пишем класс Person"""

# class Person:
#     def __init__(self, name, job, pay):  # Конструктор принимает три аргумента
#         self.name = name  # self - это созданный в будущем экз.класса. name - это информ. о состоянии
#         self.job = job # job - это переменная из вне, которую мы сохраняем в классе как self.job,что бы использовать позже.
#         self.pay = pay
class Person:
    """Персонаж может не иметь работы и соответственно зарплаты"""
    def __init__(self, name, job=None, pay=0):
        if isinstance(name,str):
            self.name = name
        else:
            raise "Ошибка ввода"
        self.job = job
        self.pay = pay
    def __str__(self):
        return f'Имя: {self.name}\nДолжность: {self.job}\nЗП: {self.pay}'

P = Person('Илья','Bus',1500)
print(P)
