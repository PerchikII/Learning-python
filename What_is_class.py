"""Итерируемые объекты.
     __iter__ + yield """
class Squares:
    def __init__(self, start: int, stop: int):
        self.value = start
        self.stop = stop

    def __iter__(self):
        for i in range(self.value,self.stop):
            yield i ** 2

    # def __next__(self):
    #     if self.value == self.stop:
    #         raise StopIteration
    #     self.value += 1
    #     return self.value ** 2


X = Squares(5, 9)
print(list(X))


