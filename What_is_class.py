"""Метод __call__"""
class Callee:
    def __init__(self,data):
        self.data = data
    def __call__ (self, other):   # Перехватывает вызовы экземпляра
        print('Called:', other)
        return self.data * other

class Callee:
    def __call__(self, *pargs, **kargs):
        print('Called:',pargs,kargs)

if __name__ == '__main__':
    C = Callee(5)
    print(C(3))
