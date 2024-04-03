"""Вложенные классы:
правила областей видимости LEGB. """
print('-' * 40)
X = 100


def nester():
    X = 30
    print(f'Ф-ция nester X= {X}')

    class C:
        X = "Атрибут класса С"
        print(X)

        def method_1(self):
            print(f'Обл.видим в ф-ции method_1 X= {X}')
            print(f'{self.X} в method_1')

        def method_2(self):
            X = 3
            print(f'Локальная об.видимости method_2 Х={X}')
            self.X = 333
            print(f'Экзепляру класса определили атрибут {self.X}')

    I = C()
    I.method_1()
    I.method_2()


print(f'Глобальная область ур-нь модуля X= {X}')
nester()
print('-' * 40)
