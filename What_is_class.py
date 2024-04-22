"""Метод вызывается только через класс и никогда через экземпляр"""


class Selfless:
    def __init__(self, data):
        self.data = data

    def selfless(arg1, arg2):       # Простая функция в Python З.Х
        return arg1 + arg2

    def normal(self, arg1, arg2):  # При вызове ожидается экземпляр
        return self.data + arg1 + arg2


if __name__ == '__main__':
    X = Selfless(2)
    print(X.normal(3, 4))
    print(Selfless.normal(X, 3, 4))
    print(Selfless.selfless(3, 4))
