"""Членство:
Если __iter__ и __contains__ отсутствуют,
 работает __getitem__"""


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):       # Запасной вариант для итерации
        print(f'get {i}:', end='')  # Также для индексирования, нарезания
        return self.data[i]

    # def __iter__(self):             # Предпочтительнее для итерации
    #     print('iter=> ', end=' ')  # Допускает только один активный итератор
    #     for i in self.data:
    #         yield i
    #         print('next:', end='')

    def __next__(self):
        print('next:::', end='')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    # def __contains__(self, x):
    #     print('contains:', end='')
    #     return x in self.data


if __name__ == '__main__':
    X = Iters([44, 77, 99, 140, 417])
    print(44 in X)       # первым вызывается метод __contains__
    """Запускаем цикл- отрабатывает __iter__, который стал генератором"""
    for i in X:
        print(i, end=' II ')

    print()
    print([i ** 2 for i in X])
    print(list(map(bin, X)))
    I = iter(X)
    while True:
        try:
            print(next(I), end='')
        except StopIteration:
            break
