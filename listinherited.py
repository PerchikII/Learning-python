class Listinherited:
    """Применяет dir() для сбора атрибутов экземпляра и имен, унаследованных
из его классов; в Python З.Х отображается больше имен, чем в Python 2.Х из-за наличия
подразумеваемого суперкласса object в модели классов нового стиля;
getattr() извлекает унаследованные имена не в self.__diet__;
используйте __str__ , а не __ rерr__ , иначе произойдет зацикливание при
вызове связанных методов!"""

    def __attrnames(self, indent=' ' * 4):
        result = 'Unders%s\n%s%%s\nOthers%s\n' % ('-' * 77, indent, '-' * 77)
        unders = []
        for attr in dir(self):
            if attr[: 2] == '__' and attr[-2:] == '__':
                unders.append(attr)
            else:
                display = str(getattr(self, attr))[:82 - (len(indent) + len(attr))]
                result += '%s%s=%s\n' % (indent, attr, display)
        return result % ','.join(unders)
    def __str__ (self) :
        return (f'Instance of {self.__class__.__name__}\n'
                f'address {id(self)}:\n'
                f'атрибуты:\n {self.__attrnames()}')


if __name__ == '__main__':
    import testmixin

    testmixin.tester(Listinherited)
