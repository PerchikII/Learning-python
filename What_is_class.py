"""Методы являются объектами:
связанные или несвязанные методы"""

class Spam:
    def doit(self, message):
        print(message)


if __name__ == '__main__':
    obj = Spam()
    obj.doit('hello world')

    objectl = Spam()
    х = objectl.doit         # Объект связанного метода: экземпляр + функция
    х('hello world')


    objectl = Spam()
    t = Spam.doit           # Объект несвязанного метода
    t(objectl, 'howdy')

