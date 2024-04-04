"""Индексирование и нарезание:
             методы
 __getitem__(self, index),
 __setitem__(self, key, value)
 __delitem__(self, key)"""


class C:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        """Вызывается для индексирования или нарезания"""
        print('getitem:', [x for x in dir(index) if not x.startswith('__')])
        return self.data[index]

    def __setitem__(self, key, value):
        self.data[key] = value
        return self.data

    def __delitem__(self, key):
        del self.data[key]
        return self.data



I = C()
print(I[2:5:2])
print(I[slice(2, None)])

I[0]=50
print(I.data)

del I[3]
print(I.data)
