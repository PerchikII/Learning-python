import importlib

def tester(listerclass, sept=False) :
    class Super:
        def __init__(self):
            self.datal = 'spam'
        def ham(self) :
            pass
    class Sub(Super, listerclass):
        def __init__(self):
            Super.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 42
        def spam(self):
            pass
    instance = Sub()
    print(instance)
    if sept: print('-' * 80)

def testByNames(modname, classname, sept=False):
    modobject = importlib.import_module(modname)
    listerclass = getattr(modobject, classname)
    tester(listerclass, sept)


if __name__ == '__main__' :
    testByNames('listinstance', 'Listinstance', True)