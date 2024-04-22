"""Информация для интроспекции объектов связанных методов"""

class Number:
    def __init__(self, base):
        self .base = base
    def double (self):
        return self.base * 2
    def triple(self):
        return self.base * 3

if __name__ == '__main__':
    x = Number(2)
    у = Number(3)
    z = Number(4)
    bound = x.double
    print(bound.__self__)
    print(x.double.__self__)
    print(bound.__self__.base)  # Значение, которое получил экз при создании.
    print(bound.__func__)
    print(bound())


    # acts = [x.double, у.double, у.triple, z.double] # Список связанных методов
    # for act in acts:                # Присваивание метода имени 'act'
    #     print(act())                # Вызов метода