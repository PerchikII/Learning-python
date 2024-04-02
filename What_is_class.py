"""Вложенные классы:
правила областей видимости LEGB. Присваиваем значение
тому же самому имени на уровнях вложенных функций."""

X = 1
def nester():
    X = 2
    print(X,'ф-ция nester')
    class C:
        print(X,'класс С')
        def method_1(self):
            print(X,'method_1')
        def method_2(self):
            X = 3
            print(X,'method_2')
    I = C()
    I.method_1()
    I.method_2()
print(X,"Глобальный")
nester()
print('-' * 40)
