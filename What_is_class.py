"""Итерируемые объекты.
 Итерируемые объекты, определяемые пользователем.
            методы
    __iter__ и __next__"""
class Squares:
    def __init__(self, start: int, stop: int):  # Сохранить состояние при создании
        self.value = start - 1
        self.stop = stop

    def __iter__(self):  # Получить объект итератора при вызове iter
        return self

    def __next__(self):  # Возвратить квадрат на каждой итерации
        if self.value == self.stop:  # Также вызывается встроенной функцией next
            raise StopIteration
        self.value += 1
        return self.value ** 2


X = Squares(5, 9)
I = iter(X)
   # ИЛИ
print(list(X))
