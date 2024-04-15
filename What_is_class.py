"""Эмуляция защиты атрибутов экземпляра: часть 1"""


class PrivateExc(Exception): pass


class Privacy:
    def __setattr__(self, attrname, value):
        """ Если передаваемый атрибут присутствует в атр.класса,
        падает ошибка, если нет- присваевается."""
        if attrname in self.privates:
            raise PrivateExc(f'Заданный атрибут {attrname} находится в списке атр.класса', self)
        else:
            self.__dict__[attrname] = value


class Test1(Privacy):
    """ Экз.класса защищён от нового присваивания возраста """
    privates = ['age']


class Test2(Privacy):
    """ Экз.класса защищён от нового присваивания имени и оплаты """
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Tom'



if __name__ == '__main__':
    x = Test1()
    y = Test2()
    x.name = 'Bob'
    x.age = 22
    #y.name = 'Sue'
    print(x.name)
    y.pa = 44
    y.age = 30
    print(y.name,y.age,y.pa)
    # x.age = 40
    # print(y.age)
